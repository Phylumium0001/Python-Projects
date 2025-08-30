from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class BaseUrl(BaseModel):
    url: str


class PostResponse(BaseModel):
    long_url: str
    short_url: str

# GET /<shortcode>


@app.get("/{short_code}")
def unshorten(url):
    # Match Found
    # Redirect the user to the page :  RedirectResponse(url)

    # Match Not Found
    pass

# POST /shorten


@app.post("/shorten")
def shorten(new_url, response_model=PostResponse):
    pass
