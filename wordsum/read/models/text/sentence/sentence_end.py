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
'''
class Sentence_End(object):

        def __init__(self, pattern = None):

                mark_begin_string = "^''|^\"|^,,|^<|^>|"
                mark_end_string =  "!''$|!\"$|!<$|!>$|\?''$|\?\"$|\?<$|\?>$|\.''$|\.\"$|\.<$|\.>$|\.$|!$|\?$|"
                mark_narrator_end_string = "!\s+|\.\s+|\?\s+|"
                mark_dialog_end_string = "\.''\s+|\?''\s+|!''\s+|\.>\s+|\?>\s+|!>\s+|\.<\s+|\?<\s+|!<\s+|!\"\s+|\.\"\s+|\?\"\s+|"
                mark_narrator_end_dialog_begin = ",\s+>\||,\s+<\||,\s+>|,\s+<|,\s+''|,\s+,,|,\s+\"|"
                mark_dialog_begin_string = ",,|''|<\||>\||<|>"

                if pattern is None:
                        self._pattern =  "(" + mark_begin_string +  mark_end_string + mark_narrator_end_string + mark_dialog_end_string + mark_narrator_end_dialog_begin +  mark_dialog_begin_string + ")"
                else:
                        self._pattern = pattern


        @property
        def pattern(self):
                return self._pattern

        @pattern.setter
        def pattern(self, pattern):
                self._pattern  = pattern

