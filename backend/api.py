import os
import random
import requests
from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.cloud import storage
from dotenv import load_dotenv
from unsplash.api import Api
from unsplash.auth import Auth

import assets

# load credentials for image APIs
load_dotenv()
client_id = os.getenv("UNSPLASH_ACCESS_KEY")
client_secret = os.getenv("UNSPLASH_SECRET_KEY")
redirect_uri = "https://placegoat.com/1440/900"
auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)

# FASTAPI SETUP ------------------------------------------------------------------------
app = FastAPI()

# The "*" is needed for vue to accept requests when working locally
origins = ["http:localhost:3000", "http://localhost:8080", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# gcloud bucket
client = storage.Client()
bucket = client.get_bucket("rens-steven-slide-gen.appspot.com")


class Slide(BaseModel):
    title: str
    img_url: str


class Deck(BaseModel):
    name: str
    slides: List[Slide]


class RandomDeck(BaseModel):
    name: str
    n_slides: int


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


def get_photo_url(query):
    """Get the url for a random picture matching the search query"""
    photos = api.photo.random(query=query)
    return photos[0].urls.raw


@app.post("/random_deck")
def random_deck(random_deck: RandomDeck):
    # get text
    with open("../data/cipsum.txt", "r") as f:
        corpus = f.read()
    # remove newlines, split sentences and strip leading and trailing whitespaces
    lines = [
        line.strip() for line in corpus.replace("\n", "").split(".") if line is not ""
    ]
    text_lines = random.choices(lines, k=random_deck.n_slides)
    # make into  slide objects
    slides = [Slide(title=text, img_url=get_photo_url(text)) for text in text_lines]
    deck = Deck(name=random_deck.name, slides=slides)
    return make_deck(deck)


@app.get("/random_slogan")
def generate_sentence():
    verb = random.choice(assets.words["verbs"])
    adjective = random.choice(assets.words["adjectives"])
    noun = random.choice(assets.words["nouns"])
    return f"{verb} {adjective} {noun}"


@app.post("/random_deck2")
def random_deck2(random_deck: RandomDeck):
    # get text
    text_lines = [generate_sentence() for _ in range(random_deck.n_slides)]
    # make into  slide objects
    slides = [Slide(title=text, img_url=get_photo_url(text)) for text in text_lines]
    deck = Deck(name=random_deck.name, slides=slides)
    return make_deck(deck)
