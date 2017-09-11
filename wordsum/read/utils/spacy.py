import spacy
import logging



def get_spacy_en_object(text):
    logging.debug("Write object to know.")

    if text is not None:
        nlp = spacy.load('en')
        text_spacy_en_object = nlp(text)

    return text_spacy_en_object



