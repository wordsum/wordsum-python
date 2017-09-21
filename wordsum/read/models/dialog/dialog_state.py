'''
text                string
narrative_tag       string
dialog_mark         dialog_mark
dialog_identifiers  dialog_identifiers
'''






from django.db import models

class Sentence(models.Model):
    text = models.TextField()

    def __str__(self):              \
        return self.text

class Narrative_Tag(models.Model):
    dialog_object = models.TextField()

    def __str__(self):
        return self.dialog_object






'''

          "dialogState": {

            "dialogMark": [
              "(,,[A-Za-z].*)|(,,\\.+[A-Za-z].*)|([A-Za-z].*\\s,,[A-Za-z].*)",
              "(,,[A-Za-z].*\u0027\u0027)|(,,\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s,,[A-Za-z].*\u0027\u0027)|(\u0027\u0027[A-Za-z].*\u0027\u0027)|(\u0027\u0027\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*\u0027\u0027)|([A-Za-z].*,\u0027\u0027 [A-Za-z].*)|([A-Za-z].*\u0027\u0027)",
              "(,,[A-Za-z].*)|(,,\\.+[A-Za-z].*)|([A-Za-z].*\\s,,[A-Za-z].*)",
              "(,,[A-Za-z].*\u0027\u0027)|(,,\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s,,[A-Za-z].*\u0027\u0027)|(\u0027\u0027[A-Za-z].*\u0027\u0027)|(\u0027\u0027\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*\u0027\u0027)|([A-Za-z].*,\u0027\u0027 [A-Za-z].*)|([A-Za-z].*\u0027\u0027)"
            ],
            "dialogNplToken": "\u0027\u0027",
            "telepathicBeginRegex": "(\u003e[A-Za-z].*)|(\u003e\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003e[A-Za-z].*)",
            "telepathicContinueRegex": "(\u003e\\|[A-Za-z].*)|(\u003e\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003e\\|[A-Za-z].*)|([A-Za-z].*\\s\u003e\\|\\.+[A-Za-z].*)",
            "telepathicEndRegex": "(\u003e\\.+[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e\\|\\.+[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e\\|[A-Za-z].*,\u003c [A-Za-z].*)|(\u003e[A-Za-z].*,\u003c [A-Za-z].*)|([A-Za-z].*,\u003c [A-Za-z].*)|(\u003e[A-Za-z].*\u003c)|(\u003e\\.+[A-Za-z].*\u003c)|(\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e[A-Za-z].*\u003c)|(\u003e\\|[A-Za-z].*\u003c)|(\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e\\|[A-Za-z].*\u003c)|([A-Za-z].*\\s\u003e\\|\\.+[A-Za-z].*\u003c)|([A-Za-z].*\u003c)",
            "internalBeginRegex": "(\u003c[A-Za-z].*)|(\u003c\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003c[A-Za-z].*)",
            "internalContinueRegex": "(\u003c\\|[A-Za-z].*)|(\u003c\\|\\.+[A-Za-z].*)|([A-Za-z].*\\s\u003c\\|[A-Za-z].*)|([A-Za-z].*\\s\u003c\\|\\.+[A-Za-z].*)",
            "internalEndRegex": "(\u003c\\|\\.*[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c\\.*[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c\\|[A-Za-z].*,\u003e [A-Za-z].*)|(\u003c[A-Za-z].*,\u003e [A-Za-z].*)|([A-Za-z].*,\u003e [A-Za-z].*)|(\u003c[A-Za-z].*\u003e)|(\u003c\\.+[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c[A-Za-z].*\u003e)|(\u003c\\|[A-Za-z].*\u003e)|(\u003c\\|\\.+[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c\\|[A-Za-z].*\u003e)|([A-Za-z].*\\s\u003c\\|\\.+[A-Za-z].*\u003e)|([A-Za-z].*\u003e)",
            "audioBeginRegex": "(,,[A-Za-z].*)|(,,\\.+[A-Za-z].*)|([A-Za-z].*\\s,,[A-Za-z].*)",
            "audioContinueRegex": "(\u0027\u0027[A-Za-z].*)|(\u0027\u0027\\.+[A-Za-z].*)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*)|([A-Za-z].*\\s\u0027\u0027\\.+[A-Za-z].*)",
            "audioEndRegex": "(,,[A-Za-z].*\u0027\u0027)|(,,\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s,,[A-Za-z].*\u0027\u0027)|(\u0027\u0027[A-Za-z].*\u0027\u0027)|(\u0027\u0027\\.+[A-Za-z].*\u0027\u0027)|([A-Za-z].*\\s\u0027\u0027[A-Za-z].*\u0027\u0027)|([A-Za-z].*,\u0027\u0027 [A-Za-z].*)|([A-Za-z].*\u0027\u0027)",
            "telepathicBeginUnicode": "u003E",
            "telepathicContinueUnicode": "u003Eu007C",
            "telepathicEndUnicode": "u003C",
            "internalBeginUnicode": "u003C",
            "internalContinueUnicode": "u003Cu007C",
            "internalEndUnicode": "u003E",
            "audioBeginUnicode": "u002Cu002C",
            "audioContinueUnicode": "u0027u0027",
            "audioEndUnicode": "u0027u0027",
            "telepathicBeginMark": "\u003e",
            "telepathicContinueMark": "\u003e|",
            "telepathicEndMark": "\u003c",
            "internalBeginMark": "\u003c",
            "internalContinueMark": "\u003c|",
            "internalEndMark": "\u003e",
            "audioBeginMark": ",,",
            "audioContinueMark": "\u0027\u0027",
            "audioEndMark": "\u0027\u0027",
            "dialog": true,
            "dialogBegin": true,
            "dialogEnd": true,
            "dialogContinue": false
          },
'''