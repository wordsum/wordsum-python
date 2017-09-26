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

    def __init__(self,
                 dialog_continuing_mark_to_narrator = None,
                 dialog_mark_begin = None,
                 dialog_mark_end = None,
                 dialog_ending_mark = None,
                 dialog_beginning_mark = None,
                 narrator_continuing_mark_to_dialog = None,
                 narrator_ending_mark = None,
                 split = None):

        if dialog_continuing_mark_to_narrator is None:
            self._dialog_continuing_mark_to_narrator = ",\"\s+|,''\s+|,>\s+|,<\s+|"
        else:
            self._dialog_continuing_mark_to_narrator = dialog_continuing_mark_to_narrator


        if  dialog_mark_begin is None:
            self._dialog_mark_begin = "^''|^\"|^,,|^<|^>|"
        else:
            self._dialog_mark_begin =  dialog_mark_begin


        if  dialog_mark_end is None:
            self._dialog_mark_end = "!''$|!\"$|!<$|!>$|\?''$|\?\"$|\?<$|\?>$|\.''$|\.\"$|\.<$|\.>$|\.$|!$|\?$|"
        else:
            self._dialog_mark_end =  dialog_mark_end


        if  dialog_ending_mark is None:
            self._dialog_ending_mark = "\.''\s+|\?''\s+|!''\s+|\.>\s+|\?>\s+|!>\s+|\.<\s+|\?<\s+|!<\s+|!\"\s+|\.\"\s+|\?\"\s+|"
        else:
            self._dialog_ending_mark =  dialog_ending_mark


        if  dialog_beginning_mark is None:
            self._dialog_beginning_mark = ",,|''|<\||>\||<|>|\""
        else:
            self._dialog_beginning_mark =  dialog_beginning_mark


        if  narrator_continuing_mark_to_dialog is None:
            self._narrator_continuing_mark_to_dialog = ",\s+>\||,\s+<\||,\s+>|,\s+<|,\s+''|,\s+,,|,\s+\"|"
        else:
            self._narrator_continuing_mark_to_dialog =  narrator_continuing_mark_to_dialog


        if narrator_ending_mark is None:
            self._narrator_ending_mark = "!\s+|\.\s+|\?\s+|"
        else:
            self._narrator_ending_mark  = narrator_ending_mark



        if split is None:
            self._split =  "(" + self._narrator_continuing_mark_to_dialog + self._narrator_ending_mark +  self._dialog_continuing_mark_to_narrator + self._dialog_mark_begin + self._dialog_mark_end + self._dialog_ending_mark + self._dialog_beginning_mark + ")"
        else:
            self._split = split


    @property
    def dialog_continuing_mark_to_narrator(self):
        return self._dialog_continuing_mark_to_narrator

    @dialog_continuing_mark_to_narrator.setter
    def dialog_continuing_mark_to_narrator(self, dialog_continuing_mark_to_narrator):
        self._dialog_continuing_mark_to_narrator = dialog_continuing_mark_to_narrator


    @property
    def dialog_mark_begin(self):
        return self._dialog_mark_begin

    @dialog_mark_begin.setter
    def dialog_mark_begin(self, dialog_mark_begin):
        self._dialog_mark_begin = dialog_mark_begin


    @property
    def dialog_mark_end(self):
        return self._dialog_mark_end

    @dialog_mark_end.setter
    def dialog_mark_end(self, dialog_mark_end):
        self._dialog_mark_end = dialog_mark_end


    @property
    def dialog_ending_mark(self):
        return self._dialog_ending_mark

    @dialog_ending_mark.setter
    def dialog_ending_mark(self, dialog_ending_mark):
        self._dialog_ending_mark = dialog_ending_mark


    @property
    def dialog_beginning_mark(self):
        return self._dialog_beginning_mark

    @dialog_beginning_mark.setter
    def dialog_beginning_mark(self, dialog_beginning_mark):
        self._dialog_beginning_mark = dialog_beginning_mark


    @property
    def narrator_continuing_mark_to_dialog(self):
        return self._narrator_continuing_mark_to_dialog

    @narrator_continuing_mark_to_dialog.setter
    def narrator_continuing_mark_to_dialog(self, narrator_continuing_mark_to_dialog):
        self._narrator_continuing_mark_to_dialog = narrator_continuing_mark_to_dialog


    @property
    def narrator_ending_mark(self):
        return self._narrator_ending_mark

    @narrator_ending_mark.setter
    def narrator_ending_mark(self, narrator_ending_mark):
        self._narrator_ending_mark = narrator_ending_mark


    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, split):
        self._split  = split


