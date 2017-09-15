# Open Story License
#
# Story: wordsum-python
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

import logging

import wordsum.read.utils.spacy


def test_get_spacy_en_object():
    logging.debug("Write object to know.")

    test_sentence = "I write a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object.text == test_sentence





