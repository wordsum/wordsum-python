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

