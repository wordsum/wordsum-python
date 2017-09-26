'''
telepathic_begin_regex
telepathic_continue_regex
telepathic_end_regex

internal_begin_regex
internal_continue_regex
internal_end_regex

audio_begin_regex
audio_continue_regex
audio_end_regex

'''
class Dialog_Pattern:

    def __init__(self):

        self.telepathic_begin_regex = "(>[A-Za-z].*)|(>\\.+[A-Za-z].*)|([A-Za-z].*\\s>[A-Za-z].*)",
        self.telepathic_continue_regex = "(>\\|[A-Za-z].*)|(>\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s>\\|[A-Za-z].*)|([A-Za-z].*\\s>\\|\\.+[A-Za-z].*)"
        self.telepathic_end_regex = "(>\\.+[A-Za-z].*,< [A-Za-z].*)|(>\\|\\.+[A-Za-z].*,< [A-Za-z].*)|(>\\|[A-Za-z].*,< [A-Za-z].*)|(>[A-Za-z].*,< [A-Za-z].*)|([A-Za-z].*,< [A-Za-z].*)|(>[A-Za-z].*<)|(>\\.+[A-Za-z].*<)|(>\\|\\.+[A-Za-z].*<)|([A-Za-z].*\\s>[A-Za-z].*<)|(>\\|[A-Za-z].*<)|(>\\|\\.+[A-Za-z].*<)|([A-Za-z].*\\s>\\|[A-Za-z].*<)|([A-Za-z].*\\s>\\|\\.+[A-Za-z].*<)|([A-Za-z].*<)"

        self.internal_begin_regex = "(<[A-Za-z].*)|(<\\.+[A-Za-z].*)|([A-Za-z].*\\s<[A-Za-z].*)"
        self.internal_continue_regex = "(<\\|[A-Za-z].*)|(<\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s<\\|[A-Za-z].*)|([A-Za-z].*\\s<\\|\\.+[A-Za-z].*)"
        self.internal_end_regex  = "(<\\|\\.*[A-Za-z].*,> [A-Za-z].*)|(<\\.*[A-Za-z].*,> [A-Za-z].*)|(<\\|[A-Za-z].*,> [A-Za-z].*)|(<[A-Za-z].*,> [A-Za-z].*)|([A-Za-z].*,> [A-Za-z].*)|(<[A-Za-z].*>)|(<\\.+[A-Za-z].*>)|([A-Za-z].*\\s<[A-Za-z].*>)|(<\\|[A-Za-z].*>)|(<\\|\\.+[A-Za-z].*>)|([A-Za-z].*\\s<\\|[A-Za-z].*>)|([A-Za-z].*\\s<\\|\\.+[A-Za-z].*>)|([A-Za-z].*>)"

        self.audio_begin_regex = "(,,[A-Za-z].*)|(,,\\.+[A-Za-z].*)|([A-Za-z].*\\s,,[A-Za-z].*)"
        self.audio_continue_regex = "(''[A-Za-z].*)|(''\\.+[A-Za-z].*)|([A-Za-z].*\\s''[A-Za-z].*)|([A-Za-z].*\\s''\\.+[A-Za-z].*)"
        self.audio_end_regex ="(,,[A-Za-z].*'')|(,,\\.+[A-Za-z].*'')|([A-Za-z].*\\s,,[A-Za-z].*'')|(''[A-Za-z].*'')|(''\\.+[A-Za-z].*'')|([A-Za-z].*\\s''[A-Za-z].*'')|([A-Za-z].*,'' [A-Za-z].*)|([A-Za-z].*'')"

        '''
    Telepathic
    '''
    @property
    def telepathic_begin_regex(self):
        return self.telepathic_begin_regex

    @telepathic_begin_regex.setter
    def telepathic_begin_regex(self, telepathic_begin_regex):
        self.telepathic_begin_regex = telepathic_begin_regex

    @property
    def telepathic_continue_regex(self):
        return self.telepathic_continue_regex

    @telepathic_continue_regex.setter
    def telepathic_continue_regex(self, telepathic_continue_regex):
        self.telepathic_continue_regex = telepathic_continue_regex

    @property
    def telepathic_end_regex(self):
        return self.telepathic_end_regex

    @telepathic_end_regex.setter
    def telepathic_end_regex(self, telepathic_end_regex):
        self.telepathic_end_regex = telepathic_end_regex


    '''
    Internal
    '''
    @property
    def internal_begin_regex(self):
        return self.internal_begin_regex

    @internal_begin_regex.setter
    def internal_begin_regex(self, internal_begin_regex):
        self.internal_begin_regex = internal_begin_regex

    @property
    def internal_continue_regex(self):
        return self.internal_continue_regex

    @internal_continue_regex.setter
    def internal_continue_regex(self, internal_continue_regex):
        self.internal_continue_regex = internal_continue_regex

    @property
    def internal_end_regex(self):
        return self.internal_end_regex

    @internal_end_regex.setter
    def internal_end_regex(self, internal_end_regex):
        self.internal_end_regex = internal_end_regex


    '''
    Audio
    '''
    @property
    def audio_begin_regex(self):
        return self.audio_begin_regex

    @audio_begin_regex.setter
    def audio_begin_regex(self, audio_begin_regex):
        self.audio_begin_regex = audio_begin_regex

    @property
    def audio_continue_regex(self):
        return self.audio_continue_regex

    @audio_continue_regex.setter
    def audio_continue_regex(self, audio_continue_regex):
        self.audio_continue_regex = audio_continue_regex

    @property
    def audio_end_regex(self):
        return self.audio_end_regex

    @audio_end_regex.setter
    def audio_end_regex(self, audio_end_regex):
        self.audio_end_regex = audio_end_regex


