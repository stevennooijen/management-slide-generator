import os
import random
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

import assets

app = FastAPI()

# CONSTANTS
URL = "https://localhost:3000/"


class Slide(BaseModel):
    title: str
    img_url: str


class Deck(BaseModel):
    slides: List[Slide]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/make_deck")
def make_deck(deck: Deck):
    output = assets.START_HTML
    for slide in deck.slides:
        output += assets.slide_html(slide.title, slide.img_url)
    output += assets.END_HTML

    n_html_files = len([f for f in os.listdir("./minimal_reveal/") if ".html" in f])
    fname = f"index{n_html_files+1}.html"
    with open(f"./minimal_reveal/{fname}", "w") as f:
        f.write(output)

    return {"url": f"{URL}/minimal_reveal/{fname}"}


def upload_blob(bucket_name: str, data: str, destination_blob_name: str):
    """Uploads data to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(
        data, content_type="text/plain", client=None, predefined_acl=None
    )

