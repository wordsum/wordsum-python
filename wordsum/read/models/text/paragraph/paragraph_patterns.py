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


Model for setting expected paragraph end to know where to split.
'''

class Paragraph_Patterns(object):

    def __init__(self, end = "\n\n", split = None):
        mark_begin_string = "^''|^\"|^,,|^<|^>|"
        mark_end_string =  "!''$|!\"$|!<$|!>$|\?''$|\?\"$|\?<$|\?>$|\.''$|\.\"$|\.<$|\.>$|\.$|!$|\?$|"
        mark_dialog_end_string = "\.''\s+|\?''\s+|!''\s+|\.>\s+|\?>\s+|!>\s+|\.<\s+|\?<\s+|!<\s+|!\"\s+|\.\"\s+|\?\"\s+|"
        mark_dialog_begin_string = ",,|''|<\||>\||<|>|\""
        mark_dialog_continue_to_narrator = ",\"\s+|,''\s+|,>\s+|,<\s+|"

        mark_narrator_end_dialog_begin = ",\s+>\||,\s+<\||,\s+>|,\s+<|,\s+''|,\s+,,|,\s+\"|"
        mark_narrator_end_string = "!\s+|\.\s+|\?\s+|"


        if split is None:
            self._split =  "(" + mark_dialog_continue_to_narrator + mark_begin_string +  mark_end_string + mark_narrator_end_string + mark_dialog_end_string + mark_narrator_end_dialog_begin +  mark_dialog_begin_string + ")"
        else:
            self._split = split

        self._end = end


    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, split):
        self._split  = split


