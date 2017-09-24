
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


text	        string	                text of type string is the text of the paragraph.
order	        integer	                order of type integer is the ordinal placement of the paragraph of a File Model state.
wordCount	    integer	                wordCount of type integer is the amount of words of the paragraphText.
sentenceCount	integer	                sentenceCount of type integer is the amount of sentences of the paragraphText.
dialog	        boolean	                dialog of type boolean is of the paragraphText.
tense	        list of strings	        tense of type list of strings is a list of tenses of the paragraphText.
sentenceStates	list of SentenceStates  sentenceStates of type list of SentenceStates is a list of Sentence Model states of the Paragraph Model state.
'''
class Paragraph_State:

    def __init__(self):
        self = self


    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
        self.text  = text

    @property
    def sentence_states(self):
        return self.sentence_states

    @sentence_states.setter
    def sentence_states(self, sentence_states):
        self.sentence_states  = sentence_states