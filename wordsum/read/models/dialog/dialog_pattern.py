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


    def __init__(self,telepathic_begin_regex, telepathic_continue_regex, telepathic_end_regex,
                    internal_begin_regex, internal_continue_regex, internal_end_regex,
                    audio_begin_regex, audio_continue_regex, audio_end_regex):

        self.telepathic_begin_regex = telepathic_begin_regex
        self.telepathic_continue_regex = telepathic_continue_regex
        self.telepathic_end_regex = telepathic_end_regex

        self.internal_begin_regex = internal_begin_regex
        self.internal_continue_regex = internal_continue_regex
        self.internal_end_regex = internal_end_regex

        self.audio_begin_regex = audio_begin_regex
        self.audio_continue_regex = audio_continue_regex
        self.audio_end_regex = audio_end_regex

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






'''
    "telepathicBeginRegex": "(\u003e[A-Za-z].*)|(\u003e\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003e[A-Za-z].*)",
    "telepathicContinueRegex": "(\u003e\\|[A-Za-z].*)|(\u003e\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003e\\|[A-Za-z].*)|([A-Za-z].*\\s\u003e\\|\\.+[A-Za-z].*)",
    "telepathicEndRegex": "(\u003e\\.+[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e\\|\\.+[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e\\|[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e[A-Za-z].*,\u003c [A-Za-z].*)|([A-Za-z].*,\u003c [A-Za-z].*)|(\u003e[A-Za-z].*\u003c)|(\u003e\\.+[A-Za-z].*\u003c)|(\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e[A-Za-z].*\u003c)|(\u003e\\|[A-Za-z].*\u003c)|(\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e\\|[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\u003c)",
    "internalBeginRegex": "(\u003c[A-Za-z].*)|(\u003c\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003c[A-Za-z].*)",
    "internalContinueRegex": "(\u003c\\|[A-Za-z].*)|(\u003c\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003c\\|[A-Za-z].*)|([A-Za-z].*\\s\u003c\\|\\.+[A-Za-z].*)",
    "internalEndRegex": "(\u003c\\|\\.*[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c\\.*[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c\\|[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c[A-Za-z].*,\u003e [A-Za-z].*)|([A-Za-z].*,\u003e [A-Za-z].*)|(\u003c[A-Za-z].*\u003e)|(\u003c\\.+[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c[A-Za-z].*\u003e)|(\u003c\\|[A-Za-z].*\u003e)|(\u003c\\|\\.+[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c\\|[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c\\|\\.+[A-Za-z].*\u003e)|([A-Za-z].*\u003e)",
    "audioBeginRegex": "(,,[A-Za-z].*)|(,,\\.+[A-Za-z].*)|([A-Za-z].*\\s,,[A-Za-z].*)",
    "audioContinueRegex": "(\u0027\u0027[A-Za-z].*)|(\u0027\u0027\\.+[A-Za-z].*)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*)|([A-Za-z].*\\s\u0027\u0027\\.+[A-Za-z].*)",
    "audioEndRegex": "(,,[A-Za-z].*\u0027\u0027)|(,,\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s,,[A-Za-z].*\u0027\u0027)|(\u0027\u0027[A-Za-z].*\u0027\u0027)|(\u0027\u0027\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*\u0027\u0027)|([A-Za-z].*,\u0027\u0027 [A-Za-z].*)|([A-Za-z].*\u0027\u0027)",

'''

