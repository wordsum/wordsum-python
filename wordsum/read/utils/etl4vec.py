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
Functions to read a wordsum text model and create data for word2vec.py and begin
to create teh story model.
'''
import logging
import itertools


'''
R E P L A C E   P U N C T U A T I O N   I N   S T O R Y
'''

'''
Replace punctuation.
'''
def replace_punctuation_sentence(sentence):
    logging.debug("Grooming :", sentence)

    list_replace_no_space = ['\\u0027','\\u003c','\\u003e','|','.',',',':',';','?','<','>']

    for item in list_replace_no_space:
        sentence = sentence.replace(item, '')

    list_replace = ['\\n','...',' - ']

    for item in list_replace:
        sentence = sentence.replace(item, ' ')

    sentence = sentence.lower()

    return sentence

'''
Replace punctuation in a paragraph
'''
def replace_punctuation_paragraph(paragraph):
    logging.debug('replacing patterns in paragraph.')

    for i, s in enumerate(paragraph):
        paragraph[i] = replace_punctuation_sentence(s)

    return paragraph

'''
Replace punctuation in a story
'''
def replace_punctuation_story(story):
    logging.debug("replace punctuation in story.")

    for i, p in enumerate(story):
        story[i] = replace_punctuation_paragraph(p)

    return story

'''
L I S T   S E N T E N C E    I N   S T O R Y
'''

'''
list sentence, so it is easier to vector or put into a neural netowrk.
'''
def list_sentence(string_sentence):
    logging.debug("list_sentence")

    if string_sentence is not None:
        words = string_sentence.split()
        words = [x.strip(' ') for x in words]
    else:
        words = None

    return words

'''
list sentence string in the paragraph array.
'''
def list_sentences_in_paragraph(paragraph):
    logging.debug('list_sentence_in_paragraph')

    for i, s in enumerate(paragraph):
        paragraph[i] = list_sentence(s)

    return paragraph


'''
list sentence in a the story array.
'''
def list_sentences_in_story(story):
    logging.debug('list_sentence_in_story')

    for i, p in enumerate(story):
        story[i] = list_sentences_in_paragraph(p)

    return story


'''
Make a list with all story lists into one.
'''
def list_story_lists(story):
    logging.debug("list_story lists")

    story_list = []

    if story is not None:
        story_list = list(itertools.chain.from_iterable(story))

    return story_list



