from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

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


@app.get("/", response_class=HTMLResponse)
def home():
    return homepage

# GET /<shortcode>


def get_url_from_db(short_code: str):
    short_url = "shlk.com/" + short_code
    res = db.find_url(short_url)
    if not res:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return res


@app.get("/api/{short_code}")
def unshorten_api(short_code: str):
    long_url = get_url_from_db(short_code)
    # This endpoint returns JSON
    return {"short_url": short_code, "long_url": long_url}


@app.get("/{short_code}")
def unshorten(short_code: str):
    print(short_code)
    long_url = get_url_from_db(short_code)
    # This endpoint redirects the user
    return RedirectResponse(url=long_url, status_code=307)


@app.get("/api/urls")
def get_urls():
    urls = db.get_all_url()
    print(urls)
    # res = []
    # for url in urls:
    #     res.append(URLResponse(short_url=url[0], long_url=url[1]))

    return urls

# POST /shorten


@app.post("/shorten", response_model=URLResponse)
def shorten(long_url: URLRequest):
    normalized_url = normalize_url(long_url.long_url)
    hash_value = generate_hash_value(normalized_url)
    short_url = generate_url(hash_value)

    db.add_new_url(short_url, long_url.long_url)

    # Return an instance of the Pydantic model
    return URLResponse(short_url=short_url, long_url=long_url.long_url)
