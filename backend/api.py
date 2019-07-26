import os
import random
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import storage
import assets

app = FastAPI()

client = storage.Client()
bucket = client.get_bucket("rens-steven-slide-gen.appspot.com")

# CONSTANTS
URL = "https://localhost:3000/"


class Slide(BaseModel):
    title: str
    img_url: str


class Deck(BaseModel):
    name: str
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

    blob = bucket.blob(f"minimal_reveal/{deck.name}.html")
    blob.upload_from_string(output, content_type="text/html")
    return {
        "destination": f"https://storage.googleapis.com/rens-steven-slide-gen.appspot.com/minimal_reveal/{deck.name}.html"
    }


