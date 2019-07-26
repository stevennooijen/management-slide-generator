import spacy


def text_essence_extractor(sentence, nouns=True, verbs=True):
    """
    Uses spaCy to extract essence of a sentence using the part of speech tagger.
    If nouns and verbs are both False, use noun_chunks

    :param sentence: string input sentence
    :param nouns: whether to return nouns
    :param verbs: whether to return verbs

    :return: string with nouns and/or verbs
    """

    # load language model and create nlp object
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)

    # parse elements
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    noun_spans = [chunk.root.text for chunk in doc.noun_chunks]
    verb_spans = [token.text for token in doc if token.dep_ == 'ROOT' and token.pos_ == 'VERB']

    if nouns:
        if verbs:
            essence = noun_spans + verb_spans
        else:
            essence = noun_spans
    else:
        if verbs:
            essence = verb_spans
        else:
            essence = noun_chunks

    return ' '.join(essence)
