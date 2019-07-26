import os

from dotenv import load_dotenv

from unsplash.api import Api
from unsplash.auth import Auth


class Unsplash:

    def __init__(self):

        # load credentials for image APIs
        load_dotenv()

        # set credentials
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("SECRET_KEY")
        redirect_uri = os.getenv('REDIRECT_URI')

        # create api object
        auth = Auth(client_id, client_secret, redirect_uri)
        self.api = Api(auth)

    def get_photo_url(self, query):
        """Get the url for a random picture matching the search query"""
        photos = self.api.photo.random(query=query)
        return photos[0].urls.raw
