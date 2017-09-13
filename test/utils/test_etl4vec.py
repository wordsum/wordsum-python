'''
Tests for wordsum.read.etl4vec
'''

import json
import pytest
import wordsum.read.utils.etl4vec
import os

TEST_PARAGRAPH = ['This leads to a paragraph\\n\\nThis leads TO\\u0027 and\\u003c or this ',
               '\\u003eand talking To the| for comma ,,Mistake in misunderstanding this...Or. OR,',
               ' when to end the sentence: to point right here in a series; another series?']

RETURN_PARAGRAPH = ['this leads to a paragraph  this leads to and or this ',
                  'and talking to the for comma mistake in misunderstanding this or or'
                  ' when to end the sentence to point right here in a series another series']

RETURN_LIST = ['this', 'leads', 'to', 'a', 'paragraph', 'this', 'leads', 'to', 'and', 'or', 'this']

TEST_STORY = [TEST_PARAGRAPH, TEST_PARAGRAPH]

RETURN_STORY = [RETURN_PARAGRAPH, RETURN_PARAGRAPH]



@pytest.fixture
def test_text_model():

    file_test = os.path.realpath('./') + '/data/train/plot/0001.json'

    with open(file_test) as data_file:
        test_text_model = json.load(data_file)


    return test_text_model


def test_replace_punctuation_sentence():

    sentence = wordsum.read.utils.etl4vec.replace_punctuation_sentence(TEST_PARAGRAPH[0])

    print("THE RETURN:", sentence)
    print("THE ORIGINAL:", TEST_PARAGRAPH[0])

    assert TEST_PARAGRAPH[0] != sentence
    assert RETURN_PARAGRAPH[0] == sentence

def test_list_sentence():

    words = wordsum.read.utils.etl4vec.list_sentence(RETURN_PARAGRAPH[0])

    print("THE RETURN:", words)

    assert RETURN_LIST == words


def test_replace_punctuation_paragraph():

    wordsum.read.utils.etl4vec.replace_punctuation_paragraph(TEST_PARAGRAPH)

    print("THE RETURN:", RETURN_PARAGRAPH)
    print("THE ORIGINAL:", TEST_PARAGRAPH)

    assert TEST_PARAGRAPH[0] == RETURN_PARAGRAPH[0]


def test_replace_punctuation_story():

    wordsum.read.utils.etl4vec.replace_punctuation_story(TEST_STORY)

    assert TEST_PARAGRAPH[0][0] == RETURN_PARAGRAPH[0][0]


def test_get_file_state_value():

    test_text_model = json.loads('{"fileState":"The sentence of six.", "copyright":"open"}')

    file_state = wordsum.read.utils.etl4vec.get_file_state(test_text_model)

    print("filesState: ", file_state)

    assert file_state ==  "The sentence of six."


def test_get_file_state_no_value():

    test_text_model = json.loads('{"copyright":"open"}')

    file_state = wordsum.read.utils.etl4vec.get_file_state(test_text_model)

    assert file_state ==  None


def test_get_text_model_narrator_paragraphs(test_text_model):


    test_sentence = "Towel around neck is."

    paragraphs = wordsum.read.utils.etl4vec.get_text_model_narrator_paragraphs(test_text_model)

    assert  paragraphs[0][0] == test_sentence


def test_get_paragraph_model_narrator_sentences(test_text_model):

    test_paragraph  = ['Bikers twist front wheels before taxi.', 'The bikers are dressed in leather coats and chaps with shiny studs along seams.', 'Leather bikers slowly weave through the rollers, bikers, movers and walkers.']

    sentences = wordsum.read.utils.etl4vec.get_paragraph_model_narrator_sentences(test_text_model['paragraphStates'][112])


    assert sentences == test_paragraph


def test_get_paragraph_model_dialog_sentences(test_text_model):

    test_paragraph  = '<|Late.'

    sentences = wordsum.read.utils.etl4vec.get_paragraph_model_dialog_sentences(test_text_model['paragraphStates'][246])

    assert sentences[0] == test_paragraph

