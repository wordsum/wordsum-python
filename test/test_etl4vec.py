'''
Tests for wordsum.read.etl4vec
'''

import wordsum.read.etl4vec
import json
import os

# TODO: OPEN ONCE
FILE_TEST = os.path.realpath('./') + '/data/train/plot/0001.json'

def test_groom_string4vec():

    test_string = ("This leads to a paragraph\\n\\nThis leads TO\\u0027 and\\u003c or this "
                  "\\u003eand talking To the| for comma ,,Mistake in misunderstanding this...Or. OR,"
                  " when to end the sentence: to point right here in a series; another series?"
    )

    groomed_string = ("this leads to a paragraph  this leads to and or this and talking to the for comma mistake in "
                  "misunderstanding this or or when to end the sentence to point right here in a series another series")

    return_string = wordsum.read.etl4vec.groom_string4vec(test_string)

    print("THE RETURN:", return_string)
    print("THE ORIGINAL:", test_string)

    assert test_string != return_string
    assert groomed_string == return_string

def test_get_file_state_value():

    test_text_model = json.loads('{"fileState":"The sentence of six.", "copyright":"open"}')

    file_state = wordsum.read.etl4vec.get_file_state(test_text_model)

    print("filesState: ", file_state)

    assert file_state ==  "The sentence of six."


def test_get_file_state_no_value():

    test_text_model = json.loads('{"copyright":"open"}')

    file_state = wordsum.read.etl4vec.get_file_state(test_text_model)

    assert file_state ==  None


def test_get_text_model_narrator_paragraphs():


    test_sentence = "Towel around neck is."

    with open(FILE_TEST) as data_file:
        test_text_model = json.load(data_file)

    paragraphs = wordsum.read.etl4vec.get_text_model_narrator_paragraphs(test_text_model)

    assert  paragraphs[0][0] == test_sentence


def test_get_paragraph_model_narrator_sentences():

    test_paragraph  = ['Bikers twist front wheels before taxi.', 'The bikers are dressed in leather coats and chaps with shiny studs along seams.', 'Leather bikers slowly weave through the rollers, bikers, movers and walkers.']

    with open(FILE_TEST) as data_file:
        test_text_model = json.load(data_file)

    sentences = wordsum.read.etl4vec.get_paragraph_model_narrator_sentences(test_text_model['paragraphStates'][112])


    assert sentences == test_paragraph


def test_get_paragraph_model_dialog_sentences():

    test_paragraph  = '<|Late.'

    with open(FILE_TEST) as data_file:
        test_text_model = json.load(data_file)

    sentences = wordsum.read.etl4vec.get_paragraph_model_dialog_sentences(test_text_model['paragraphStates'][246])


    assert sentences[0] == test_paragraph

