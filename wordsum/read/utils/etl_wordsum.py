import logging



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

'''

'''
def get_paragraph_model_narrator_with_dialog_sentences(paragraph_model):
    logging.debug("Getting get_paragraph_model_narrator_with_dialog_sentences")
    paragraph = []

    for sentence_model in paragraph_model['sentenceStates']:
        if sentence_model['dialogState']['dialog'] == True:

            paragraph.append(sentence_model['sentence'])

    return paragraph