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
class Paragraph_Tags:

    def __init__(self, base=None, narrative=None, dialog=None, syntax=None, no_tag=None):

        if base is None:
            self._base = "OBJECT_"
        else:
            self._base = base

        if narrative is None:
            self._narrative = "NARRATIVE_OBJECT_"
        else:
            self._narrative = narrative

        if dialog is None:
            self._dialog = "DIALOG_OBJECT_"
        else:
            self._dialog = dialog

        if syntax is None:
            self._syntax = "PUNCTUATION_OBJECT_"
        else:
            self._syntax = syntax

        if syntax is None:
            self._no_tag = "NO_TAG"
        else:
            self._no_tag = no_tag

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base


    @property
    def narrative(self):
        return self._narrative

    @narrative.setter
    def narrative(self, narrative):
        self._narrative = narrative


    @property
    def dialog(self):
        return self._dialog

    @dialog.setter
    def dialog(self, dialog):
        self._dialog_mark = dialog


    @property
    def syntax(self):
        return self._syntax

    @syntax.setter
    def syntax(self,syntax):
        self._syntax = syntax


    @property
    def no_tag(self):
        return self._no_tag

    @no_tag.setter
    def no_tag(self,no_tag):
        self._no_tag = no_tag