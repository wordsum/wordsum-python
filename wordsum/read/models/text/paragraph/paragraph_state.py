
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


text	            string	                text of type string is the text of the paragraph.
order	            integer	                order of type integer is the ordinal placement of the paragraph of a File Model state.
word_count	        integer	                word_count of type integer is the amount of words of the paragraphText.
sentence_count	    integer	                sentence_count of type integer is the amount of sentences of the paragraphText.
dialog	            boolean	                dialog of type boolean is of the paragraphText.
tense	            list of strings	        tense of type list of strings is a list of tenses of the paragraphText.
sentence_end        list of patterns         sentence_end of type list of patterns defining end of sentences.
sentence_states     list of sentence__states sentence_states of type list of SentenceStates is a list of Sentence Model states of the Paragraph Model state.
'''
class Paragraph_State(object):

    def __init__(self, text = None, paragraph_array = None, sentence_states = None, sentence_end = None):
        self._text = text
        self._paragraph_array = paragraph_array
        self._sentence_states = sentence_states
        self._sentence_end = sentence_end


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text  = text

    @property
    def paragraph_array(self):
        return self._paragraph_array

    @paragraph_array.setter
    def paragraph_array(self, paragraph_array):
        self._paragraph_array  = paragraph_array

    @property
    def sentence_states(self):
        return self._sentence_states

    @sentence_states.setter
    def sentence_states(self, sentence_states):
        self._sentence_states  = sentence_states

    @property
    def sentence_end(self):
        return self._sentence_end

    @sentence_end.setter
    def sentence_end(self, sentence_end):
        self._sentence_end  = sentence_end