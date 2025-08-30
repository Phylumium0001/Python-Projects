from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from utils.generate_short_url import generate_url
from utils.hash_url import generate_hash_value
from utils.normalize import normalize_url
from utils.database import Database

app = FastAPI()


class BaseUrl(BaseModel):
    url: str


class PostResponse(BaseModel):
    long_url: str
    short_url: str

# GET /<shortcode>


@app.get("/{short_code}")
def unshorten(short_code: str):
    url = "shlk.com/" + short_code

    print(url)

    # Match Found
    db = Database()
    res = db.find_url(url)
    print(f"%%%%%%%%%%%%%%%%%{res}%%%%%%%%%%%%%%%%%%%")

    if res:
        # Redirect the user to the page :  RedirectResponse(url)
        short_url, long_url = res
        return RedirectResponse(url=long_url, status_code=307)

        # return {"long_url": long_url, "short_url": short_url}

    # Match Not Found
    else:
        HTTPException(status_code=404, detail="Page Not Found")

# POST /shorten


@app.post("/shorten")
def shorten(long_url: str) -> PostResponse:
    normalized_url = normalize_url(long_url)
    hash = generate_hash_value(normalized_url)
    short_url = generate_url(hash)

    # TODO : Store to database

    # Return the Response
    if short_url:
        return {"long_url": long_url, "short_url": short_url}
    else:
        HTTPException(status_code=400, detail="Failed to shorten")
