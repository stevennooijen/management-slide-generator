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

# Deck Generator 

Install reveal-md

```
npm install -g reveal-md
```

Run live: reveal-md ./slides/deck.md
Export to static html: reveal-md ./slides/deck.md --static ./output/_static
Export to pdf: reveal-md ./slides/deck.md --print ./output/deck.pdf