# Management Slide Generator

Attempt to create stylish management slides from Python

## Authors

* Rens Dimmendaal
* Steven Nooijen

## Virtual environment

Set up using the `requirements.txt`:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Data

So far the only source used comes from https://www.cipsum.com/. 

It's not a lot of data so we added the file to the project. 
On the site use settings of 27  paragraphs. Adding more 
paragraphs will just repeat the first 27 over and over again.

## SpaCy language models installed

Install spaCy language models as follows:

```
python -m spacy download en_core_web_sm
```

# Run api

A deployed version of the api can be found at

[rens-steven-slide-gen.appspot.com/docs](https://rens-steven-slide-gen.appspot.com/docs)

To run locally:

Install the requirements in the backend folder
Add your Unsplash account and secret key to a .env file

```
cd ./backend/
uvicorn api:app --reload
```
Read the api docs for instructions on how to generate decks. 