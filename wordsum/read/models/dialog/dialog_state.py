'''
text                string
narrative_tag       string
dialog_mark         dialog_mark
dialog_meta         dialog_meta
dialog_pattern      dialog_pattern
'''
class Dialog_State:

    def __init__(self,text, narrative_tag, dialog_mark, dialog_meta, dialog_pattern):
        self.text = text
        self.narrative_tag = narrative_tag
        self.dialog_mark = dialog_mark
        self.dialog_meta = dialog_meta
        self.dialog_pattern = dialog_pattern
        x

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
       self.text = text



    @property
    def narrative_tag(self):
        return self.narrative_tag

    @narrative_tag.setter
    def narrative_tag(self, narrative_tag):
       self.narrative_tag = narrative_tag



    @property
    def dialog_mark(self):
        return self.dialog_mark

    @dialog_mark.setter
    def dialog_mark(self, dialog_mark):
        self.dialog_mark = dialog_mark



    @property
    def dialog_meta(self):
        return self.dialog_meta

    @dialog_meta.setter
    def dialog_meta(self, dialog_meta):
        self.dialog_meta = dialog_meta



    @property
    def dialog_pattern(self):
        return self.dialog_pattern

    @dialog_pattern.setter
    def dialog_pattern(self, dialog_pattern):
        self.dialog_pattern = dialog_pattern

