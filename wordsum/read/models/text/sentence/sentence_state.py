
'''
sentence_text	    boolean	            sentenceText of type string is the text of the sentence.
order	            integer	            order of type integer is the ordinal placement of the sentence of the Paragraph Model state.
wordCount           integer	            wordCount of type integer is the amount of words of the sentenceText.
tense	            list of strings	    tense of type list of strings is a list of tenses of the sentenceText.
nlpState	        NlpState	        nlpState of type NlpState is an Natural Language Processing Model state of the sentenceText.
punctuation_state	PunctuationState	punctuationState of type PunctuationState is a Punctuation Model state of the sentenceText.
spellcheck_state	SpellcheckState	    spellcheckState of type SpellcheckState is a Spellcheck Model state of the sentenceText.
dialog_state	    DialogState	        dialogState of type DialogState is a Dialog Model state of the sentenceText.
'''
class Sentence_State(object):

    def __init__(self, text = None, punctuation = None, tag = None, nlp_state = None, dictionary = None):
        self._text = text
        self._punctuation = punctuation
        self._tag = tag
        self._nlp_state = nlp_state
        self._dictionary =  dictionary
