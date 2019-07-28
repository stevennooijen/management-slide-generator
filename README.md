# Management Slide Generator

Attempt to create stylish management slides from Python

[Sample deck](https://storage.googleapis.com/rens-steven-slide-gen.appspot.com/minimal_reveal/random_slogans.html)

## Authors

* Rens Dimmendaal
* Steven Nooijen


## Data

**Text sources:**
* https://www.cipsum.com/
* https://www.atrixnet.com/bs-generator.html

**Image source:**
* https://unsplash.com

**Slide source:**
* https://revealjs.com

## Virtual environment

Set up using the `requirements.txt`:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

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