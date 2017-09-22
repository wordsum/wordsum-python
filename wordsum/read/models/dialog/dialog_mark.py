class Dialog_Mark:


    def __init__(self):
        self.telepathic_begin_unicode = "\u003e"
        self.telepathic_continue_unicode = "\u003E\u007C"
        self.telepathic_end_unicode = "\u003C"

        self.internal_begin_unicode = "\u003C"
        self.internal_continue_unicode = "\u003C\u007C"
        self.internal_end_unicode = "\u003e"

        self.audio_begin_unicode = "\u002C\u002C"
        self.audio_continue_unicode = "\u0027\u0027"
        self.audio_end_unicode = "\u0027\u0027"

        self.telepathic_begin_character = ">"
        self.telepathic_continue_character = ">|"
        self.telepathic_end_character = "<"

        self.internal_begin_character = "<"
        self.internal_continue_character = "<|"
        self.internal_end_character = ">"

        self.audio_begin_character = ",,"
        self.audio_continue_character = "''"
        self.audio_end_character = "''"

    '''
    Telepathic Unicode
    '''
    @property
    def telepathic_begin_unicode(self):
        return self.telepathic_begin_unicode

    @telepathic_begin_unicode.setter
    def telepathic_begin_unicode(self, telepathic_begin_unicode):
        self.telepathic_begin_unicode = telepathic_begin_unicode


    @property
    def telepathic_continue_unicode(self):
        return self.telepathic_continue_unicode

    @telepathic_continue_unicode.setter
    def telepathic_continue_unicode(self, telepathic_continue_unicode):
        self.telepathic_continue_unicode = telepathic_continue_unicode


    @property
    def telepathic_end_unicode(self):
        return self.telepathic_end_unicode

    @telepathic_end_unicode.setter
    def telepathic_end_unicode(self, telepathic_end_unicode):
        self.telepathic_end_unicode = telepathic_end_unicode


    '''
    Internal Unicode
    '''
    @property
    def internal_begin_unicode(self):
        return self.internal_begin_unicode

    @internal_begin_unicode.setter
    def internal_begin_unicode(self, internal_begin_unicode):
        self.internal_begin_unicode = internal_begin_unicode


    @property
    def internal_continue_unicode(self):
        return self.internal_continue_unicode

    @internal_continue_unicode.setter
    def internal_continue_unicode(self, internal_continue_unicode):
        self.internal_continue_unicode = internal_continue_unicode


    @property
    def internal_end_unicode(self):
        return self.internal_end_unicode

    @internal_end_unicode.setter
    def internal_end_unicode(self, internal_end_unicode):
        self.internal_end_unicode = internal_end_unicode


    '''
    Audio Unicode
    '''
    @property
    def audio_begin_unicode(self):
        return self.audio_begin_unicode

    @audio_begin_unicode.setter
    def audio_begin_unicode(self, audio_begin_unicode):
        self.audio_begin_unicode = audio_begin_unicode

    @property
    def audio_continue_unicode(self):
        return self.audio_continue_unicode

    @audio_continue_unicode.setter
    def audio_continue_unicode(self, audio_continue_unicode):
        self.audio_continue_unicode = audio_continue_unicode


    @property
    def audio_end_unicode(self):
        return self.audio_end_unicode

    @audio_end_unicode.setter
    def audio_end_unicode(self, audio_end_unicode):
        self.audio_end_unicode = audio_end_unicode





    '''
    Telepathic character
    '''
    @property
    def telepathic_begin_character(self):
        return self.telepathic_begin_character

    @telepathic_begin_character.setter
    def telepathic_begin_character(self, telepathic_begin_character):
        self.telepathic_begin_character = telepathic_begin_character


    @property
    def telepathic_continue_character(self):
        return self.telepathic_continue_character

    @telepathic_continue_character.setter
    def telepathic_continue_character(self, telepathic_continue_character):
        self.telepathic_continue_character = telepathic_continue_character


    @property
    def telepathic_end_character(self):
        return self.telepathic_end_character

    @telepathic_end_character.setter
    def telepathic_end_character(self, telepathic_end_character):
        self.telepathic_end_character = telepathic_end_character


    '''
    Internal character
    '''
    @property
    def internal_begin_character(self):
        return self.internal_begin_character

    @internal_begin_character.setter
    def internal_begin_character(self, internal_begin_character):
        self.internal_begin_character = internal_begin_character


    @property
    def internal_continue_character(self):
        return self.internal_continue_character

    @internal_continue_character.setter
    def internal_continue_character(self, internal_continue_character):
        self.internal_continue_character = internal_continue_character


    @property
    def internal_end_character(self):
        return self.internal_end_character

    @internal_end_character.setter
    def internal_end_character(self, internal_end_character):
        self.internal_end_character = internal_end_character


    '''
    Audio character
    '''
    @property
    def audio_begin_character(self):
        return self.audio_begin_character

    @audio_begin_character.setter
    def audio_begin_character(self, audio_begin_character):
        self.audio_begin_character = audio_begin_character

    @property
    def audio_continue_character(self):
        return self.audio_continue_character

    @audio_continue_character.setter
    def audio_continue_character(self, audio_continue_character):
        self.audio_continue_character = audio_continue_character


    @property
    def audio_end_character(self):
        return self.audio_end_character

    @audio_end_character.setter
    def audio_end_character(self, audio_end_character):
        self.audio_end_character = audio_end_character