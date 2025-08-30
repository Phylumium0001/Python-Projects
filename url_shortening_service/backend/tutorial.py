from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

urls = []


@app.get("/")
def home():
    return "Something"
# Store a new url
# Get existing url by providing short url


@app.post("/new_url/")
def store_new_url(new_url: str):
    print(f"*****************{new_url}*****************")
    urls.append(new_url)
    return {"urls": urls}


@app.get("/get_url/{short_url}")
# Query
def get_original_url(short_url: int) -> str:

    if urls and short_url < len(urls):
        return urls[short_url]
    else:

        HTTPException(status_code=404, detail="Item not Found")
        HTTPException(status_code=500, detail="Item not Found")
