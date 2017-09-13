'''
Functions to read a wordsum text model and create data for word2vec.py and begin
to create teh story model.
'''
import logging


'''
R E P L A C E   P U N C T U A T I O N   I N   S T O R Y
'''

'''
Replace punctuation.
'''
def replace_punctuation_sentence(sentence):
    logging.debug("Grooming :", sentence)

    list_replace_no_space = ['\\u0027','\\u003c','\\u003e','|','.',',',':',';','?','<','>']

    for item in list_replace_no_space:
        sentence = sentence.replace(item, '')

    list_replace = ['\\n','...',' - ']

    for item in list_replace:
        sentence = sentence.replace(item, ' ')

    sentence = sentence.lower()

    return sentence

'''
Replace punctuation in a paragraph
'''
def replace_punctuation_paragraph(paragraph):
    logging.debug('replacing patterns in paragraph.')

    for i, s in enumerate(paragraph):
        paragraph[i] = replace_punctuation_sentence(s)

    return paragraph

'''
Replace punctuation in a story
'''
def replace_punctuation_story(story):
    logging.debug("replace punctuation in story.")

    for i, p in enumerate(story):
        story[i] = replace_punctuation_paragraph(p)

    return story

'''
L I S T   S E N T E N C E    I N   S T O R Y
'''

'''
list sentence, so it is easier to vector or put into a neural netowrk.
'''
def list_sentence(string_sentence):
    logging.debug("list_sentence")

    if string_sentence is not None:
        words = string_sentence.split()
        words = [x.strip(' ') for x in words]
    else:
        words = None

    return words

'''
list sentence string in the paragraph array.
'''
def list_sentences_in_paragraph(paragraph):
    logging.debug('list_sentence_in_paragraph')

    for i, s in enumerate(paragraph):
        paragraph[i] = list_sentence(s)

    return paragraph


'''
list sentence in a the story array.
'''
def list_sentences_in_story(story):
    logging.debug('list_sentence_in_story')

    for i, p in enumerate(story):
        story[i] = list_sentences_in_paragraph(p)

    return story

'''
G E T    D A T A   F R O M   W O R D S U M
'''
'''
Get and check the file state is it has all the data for the word2vec.
'''
def get_file_state(text_model):
    logging.debug("Getting file state :")

    if 'fileState' in text_model:
        file_state = text_model['fileState']
    else:
        file_state = None


    return file_state


'''
Get narrator from all of the text model.

This returns a list of list paragraphs of list sentences.
'''
def get_text_model_narrator_paragraphs(text_model):
    logging.debug("Getting all the narrator sentences of a text model")
    paragraphs = []

    for paragraph_model in text_model['paragraphStates']:
        paragraphs.append(get_paragraph_model_narrator_sentences(paragraph_model))

    return paragraphs


'''
Get the the narrator sentence from a paragraph.
'''
def get_paragraph_model_narrator_sentences(paragraph_model):
    logging.debug("Getting all the narrator sentences of the paragraph model.")
    paragraph = []

    for sentence_model in paragraph_model['sentenceStates']:

        if sentence_model['dialogState']['dialog'] == False:

            paragraph.append(sentence_model['sentence'])

    return paragraph


'''
Get the the narrator sentence from a paragraph.
'''
def get_paragraph_model_dialog_sentences(paragraph_model):
    logging.debug("Getting all the dialog sentences of the paragraph model.")
    paragraph = []

    for sentence_model in paragraph_model['sentenceStates']:
        if sentence_model['dialogState']['dialog'] == True:

            paragraph.append(sentence_model['sentence'])

    return paragraph


