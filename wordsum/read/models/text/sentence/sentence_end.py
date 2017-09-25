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

        def __init__(self, narrator_end = "(?<=\\. <)|(?<=\\. >)|(?<=\\. ,,)|(?<=\\. '')|(?<=\\! <)|(?<=\\! >)|(?<=\\! ,,)|(?<=\\! '')|(?<=\\? <)|(?<=\\? >)|(?<=\\? ,,)|(?<=\\? '')",
                        narrator_end_dialog_begin = "(\\n)|(?<=\\.''\\ )|(?<=\\?''\\ )|(?<=\\!''\\ )|(?<=\\.>\\ )|(?<=\\?>\\ )|(?<=\\!>\\ )|(?<=\\.<\\ )|(?<=\\?<\\ )|(?<=\\!<\\ )",
                        dialog_end = "(?<=! )|(?<=\\. )|(?<=\\? )"):

                self._narrator_end = narrator_end
                self._narrator_end_dialog_begin = narrator_end_dialog_begin
                self._dialog_end = dialog_end


        @property
        def narrator_end(self):
                return self._narrator_end

        @narrator_end.setter
        def narrator_end(self, narrator_end):
                self._narrator_end  = narrator_end

        @property
        def narrator_end_dialog_begin(self):
                return self._narrator_end_dialog_begin

        @narrator_end_dialog_begin.setter
        def narrator_end_dialog_begin(self, narrator_end_dialog_begin):
                self._narrator_end_dialog_begin  = narrator_end_dialog_begin

        @property
        def dialog_end(self):
                return self._dialog_end

        @dialog_end.setter
        def dialog_end(self, dialog_end):
                self._dialog_end  = dialog_end