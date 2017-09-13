'''
Tests for wordsum.read.etl4vec
'''

import json
import pytest
import wordsum.read.utils.etl4vec
import os

TEST_REPLACE_PARAGRAPH = ['This leads to a paragraph\\n\\nThis leads TO\\u0027 and\\u003c or this ',
               '\\u003eand talking To the| for comma ,,Mistake in misunderstanding this...Or. OR,',
               ' when to end the sentence: to point right here in a series; another series?']

TEST_REPLACE_PARAGRAPH_COMPARE = ['this leads to a paragraph  this leads to and or this ',
                  'and talking to the for comma mistake in misunderstanding this or or'
                  ' when to end the sentence to point right here in a series another series']

TEST_REPLACE_STORY = [['This leads to a paragraph\\n\\nThis leads TO\\u0027 and\\u003c or this ',
               '\\u003eand talking To the| for comma ,,Mistake in misunderstanding this...Or. OR,',
               ' when to end the sentence: to point right here in a series; another series?'],
              ['This leads to a paragraph\\n\\nThis leads TO\\u0027 and\\u003c or this ',
               '\\u003eand talking To the| for comma ,,Mistake in misunderstanding this...Or. OR,',
               ' when to end the sentence: to point right here in a series; another series?']]

TEST_REPLACE_STORY_COMPARE = [['this leads to a paragraph  this leads to and or this ',
                 'and talking to the for comma mistake in misunderstanding this or or'
                 ' when to end the sentence to point right here in a series another series'],
                ['this leads to a paragraph  this leads to and or this ',
                 'and talking to the for comma mistake in misunderstanding this or or'
                 ' when to end the sentence to point right here in a series another series']]


TEST_LIST_PARAGRAPH = ['this leads to a paragraph  this leads to and or this ',
                    'and talking to the for comma mistake in misunderstanding this or or'
                    ' when to end the sentence to point right here in a series another series']

TEST_LIST_STORY = [['this leads to a paragraph  this leads to and or this ',
                    'and talking to the for comma mistake in misunderstanding this or or'
                    ' when to end the sentence to point right here in a series another series'],
                   ['this leads to a paragraph  this leads to and or this ',
                    'and talking to the for comma mistake in misunderstanding this or or'
                    ' when to end the sentence to point right here in a series another series']]


TEST_LISTS_STORY = [[['this', 'leads', 'to', 'a', 'paragraph', 'this', 'leads', 'to', 'and', 'or', 'this'],
                     ['and', 'talking', 'to', 'the', 'for', 'comma', 'mistake', 'in', 'misunderstanding', 'this', 'or',
                      'or', 'when', 'to', 'end', 'the', 'sentence', 'to', 'point', 'right', 'here', 'in', 'a', 'series', 'another', 'series']],
                    [['this', 'leads', 'to', 'a', 'paragraph', 'this', 'leads', 'to', 'and', 'or', 'this'],
                     ['and', 'talking', 'to', 'the', 'for', 'comma', 'mistake', 'in', 'misunderstanding', 'this', 'or',
                      'or', 'when', 'to', 'end', 'the', 'sentence', 'to', 'point', 'right', 'here', 'in', 'a', 'series', 'another', 'series']]]


TEST_SENTENCE_LIST_COMPARE = ['this', 'leads', 'to', 'a', 'paragraph', 'this', 'leads', 'to', 'and', 'or', 'this']


@pytest.fixture
def test_text_model():

    file_test = os.path.realpath('./') + '/data/train/plot/0001.json'

    with open(file_test) as data_file:
        test_text_model = json.load(data_file)


    return test_text_model

'''
T E S T   F O R   R E P L A C I N G   P U N C T U A T I O N
'''
def test_replace_punctuation_sentence():

    sentence = wordsum.read.utils.etl4vec.replace_punctuation_sentence(TEST_REPLACE_PARAGRAPH[0])

    print("THE RETURN:", sentence)
    print("THE ORIGINAL:", TEST_REPLACE_PARAGRAPH[0])

    assert TEST_REPLACE_PARAGRAPH_COMPARE[0] == sentence


def test_replace_punctuation_paragraph():

    wordsum.read.utils.etl4vec.replace_punctuation_paragraph(TEST_REPLACE_PARAGRAPH)

    print("THE NEW:", TEST_REPLACE_PARAGRAPH)

    assert TEST_REPLACE_PARAGRAPH_COMPARE[0] == TEST_REPLACE_PARAGRAPH[0]


def test_replace_punctuation_story():

    wordsum.read.utils.etl4vec.replace_punctuation_story(TEST_REPLACE_STORY)

    assert TEST_REPLACE_STORY_COMPARE[0][0] == TEST_REPLACE_STORY[0][0]

'''
T H E   L I S T   S E N T E N C E   T E S T
'''
def test_list_sentence():

    words = wordsum.read.utils.etl4vec.list_sentence(TEST_LIST_PARAGRAPH[0])

    print("THE RETURN:", words)

    assert TEST_SENTENCE_LIST_COMPARE == words

def test_list_sentences_in_paragraph():

    wordsum.read.utils.etl4vec.list_sentences_in_paragraph(TEST_LIST_PARAGRAPH)

    print("AFTER FUNCTION:", TEST_LIST_PARAGRAPH)

    assert TEST_SENTENCE_LIST_COMPARE == TEST_LIST_PARAGRAPH[0]

def test_list_sentences_in_story():

    wordsum.read.utils.etl4vec.list_sentences_in_story(TEST_LIST_STORY)

    print("AFTER FUNCTION:", TEST_LIST_STORY)

    assert TEST_SENTENCE_LIST_COMPARE == TEST_LIST_STORY[0][0]


def test_list_story_lists():

    story_list = wordsum.read.utils.etl4vec.list_story_lists(TEST_LISTS_STORY)

    assert TEST_LISTS_STORY[0][0] == story_list[0]

'''
T E S T S   T O   G E T   F I  L E   S T A T E   D A T A
'''
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

