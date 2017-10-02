'''
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


text_list_dict	    list dict	        text_list_dict of type list of a dict defining the text of the sentence.
order	            integer	            order of type integer is the ordinal placement of the sentence of the Paragraph Model state.
word_count          integer	            wordCount of type integer is the amount of words of the text_list_dict.
tense	            list of strings	    tense of type list of strings is a list of tenses of the text_list_dict.
nlp_state	        nlp_state	        nlpState of type NlpState is an Natural Language Processing Model state of the text_list_dict.
punctuation_state	punctuation_state	punctuation_state of type punctuation_state is a Punctuation Model state of the text_list_dict.
dictionary	        dictionary	    s   dictionary of type dictionary is a dictionary state of the text_list_dict.
'''
class Sentence_State(object):

    def __init__(self, text_list_dict = None, order = None, word_count = None, tense = None, nlp_state = None, dictionary = None):
        self._text_list_dict = text_list_dict
        self._order	= order
        self._word_count = word_count
        self._tense	= tense
        self._nlp_state	= nlp_state
        self._dictionary = dictionary