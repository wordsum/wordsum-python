import logging

import wordsum.read.utils.spacy


def test_get_spacy_en_object():
    logging.debug("Write object to know.")

    test_sentence = "I write a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object.text == test_sentence





