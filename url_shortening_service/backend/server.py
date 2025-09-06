import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel

from utils.generate_short_url import generate_url
from utils.hash_url import generate_hash_value
from utils.normalize import normalize_url
from utils.database import Database
from homepage import homepage

db = Database()
app = FastAPI()


class URLRequest(BaseModel):
    long_url: str


class URLResponse(BaseModel):
    short_url: str
    long_url: str
    visits: int = 0


@app.get("/", response_class=HTMLResponse)
def home():
    return homepage


def get_url_from_db(short_code: str):
    res = db.find_url(short_code)
    if not res:
        raise HTTPException(status_code=404, detail="Item Not Found")
    short_code, long_url, visits = res
    return short_code, long_url, visits


@app.get("/api/{short_code}")
def unshorten_api(short_code: str):
    short_code, long_url, visits = get_url_from_db(short_code)
    # This endpoint returns JSON
    return {"short_url": short_code, "long_url": long_url, "visits": visits}


@app.get("/{short_code}", response_class=RedirectResponse)
def unshorten(short_code: str):
    short_code, long_url, visits = get_url_from_db(short_code)
    db.increment_visit_count(short_code)

    # Normalize the URL to ensure it has a protocol before redirecting
    if long_url.startswith("http://") or long_url.startswith("https://"):
        normalized_long_url = long_url

    if long_url.startswith("www."):
        normalized_long_url = "http://" + long_url

    else:
        normalized_long_url = "http://www." + long_url

    # This endpoint redirects the user
    return RedirectResponse(url=normalized_long_url, status_code=307)


@app.get("/api/urls")
def get_urls() -> list:
    print("[All Urls] : Pending")
    urls = db.get_all_url()
    print(urls)

    if urls:
        res = [{"short_url": url[0], "long_url": url[1], "visits": url[2]}
               for url in urls]
        return res
    return []


@app.post("/shorten", response_model=URLResponse)
def shorten(long_url: URLRequest):
    normalized_url = normalize_url(long_url.long_url)
    hash_value = generate_hash_value(normalized_url)
    short_url = generate_url(hash_value)

    db.add_new_url(short_url, long_url.long_url)

    # Return an instance of the Pydantic model
    return URLResponse(short_url=short_url, long_url=long_url.long_url)
