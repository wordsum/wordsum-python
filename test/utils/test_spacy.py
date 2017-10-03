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

    test_sentence = "I write a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object.text == test_sentence


def test_get_spacy_en_object_with_subjective_pronoun():

    test_sentence = "I write a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == ""


def test_get_spacy_en_object_with_known_person_ner():

    test_sentence = "George says a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == "PERSON"


def test_get_spacy_en_object_with_known_rind_ner():

    test_sentence = "Rind says a simple sentence"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == "PERSON"


def test_get_spacy_en_object_with_known_rind_ner_DIALOG_OBJECT_1():

    test_sentence = "Rind says, DIALOG_OBJECT_1"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == "PERSON"
    assert text_spacy_object[0].dep_ == "nsubj"
    assert text_spacy_object[0].text == "Rind"
    assert text_spacy_object[0].lemma_ == "rind"
    assert text_spacy_object[0].pos_ == "PROPN"
    assert text_spacy_object[0].tag_ == "NNP"


def test_get_spacy_en_object_with_known_rind_ner_dual_verb_DIALOG_OBJECT_1():

    test_sentence = "Rind cries and says, DIALOG_OBJECT_1"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == "PERSON"
    assert text_spacy_object[0].dep_ == "compound"
    assert text_spacy_object[0].text == "Rind"
    assert text_spacy_object[0].lemma_ == "rind"
    assert text_spacy_object[0].pos_ == "PROPN"
    assert text_spacy_object[0].tag_ == "NNP"

def test_get_spacy_en_object_with_rind_but_verb_pants_also_noun():

    test_sentence = "Rind pants and says a few times, DIALOG_OBJECT_1"

    text_spacy_object = wordsum.read.utils.spacy.get_spacy_en_object(test_sentence)

    assert text_spacy_object[0].ent_type_ == ""
    assert text_spacy_object[0].dep_ == "compound"
    assert text_spacy_object[0].text == "Rind"
    assert text_spacy_object[0].lemma_ == "rind"
    assert text_spacy_object[0].pos_ == "ADJ"
    assert text_spacy_object[0].tag_ == "JJ"


