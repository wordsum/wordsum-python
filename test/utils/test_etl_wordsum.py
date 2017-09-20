import json
import os
import pytest
import wordsum.read.utils.etl_wordsum as etl_wordsum



@pytest.fixture
def test_text_model():

    file_test = os.path.realpath('./') + '/data/train/plot/The_Detective_Store/0001.json'

    with open(file_test) as data_file:
        test_text_model = json.load(data_file)


    return test_text_model

@pytest.fixture
def test_dialog_model():

    file_test = os.path.realpath('./') + '/data/train/dialog/train_rind_gets_excerpts.json'

    with open(file_test) as data_file:
        test_dialog_model = json.load(data_file)


    return test_dialog_model


'''
T E S T S   T O   G E T   F I  L E   S T A T E   D A T A
'''
def test_get_file_state_value():

    test_text_model = json.loads('{"fileState":"The sentence of six.", "copyright":"open"}')

    file_state =etl_wordsum.get_file_state(test_text_model)

    print("filesState: ", file_state)

    assert file_state ==  "The sentence of six."

def test_get_file_state_no_value():

    test_text_model = json.loads('{"copyright":"open"}')

    file_state =etl_wordsum.get_file_state(test_text_model)

    assert file_state ==  None


def test_get_text_model_narrator_paragraphs(test_text_model):


    test_sentence = "Towel around neck is."

    paragraphs =etl_wordsum.get_text_model_narrator_paragraphs(test_text_model)

    assert  paragraphs[0][0] == test_sentence


def test_get_paragraph_model_narrator_sentences(test_text_model):

    test_paragraph  = ['Bikers twist front wheels before taxi.', 'The bikers are dressed in leather coats and chaps with shiny studs along seams.', 'Leather bikers slowly weave through the rollers, bikers, movers and walkers.']

    sentences =etl_wordsum.get_paragraph_model_narrator_sentences(test_text_model['paragraphStates'][112])


    assert sentences == test_paragraph


def test_get_paragraph_model_dialog_sentences(test_text_model):

    test_paragraph  = '<|Late.'

    sentences = etl_wordsum.get_paragraph_model_dialog_sentences(test_text_model['paragraphStates'][246])

    assert sentences[0] == test_paragraph


'''
T E S T S    T O    G E T    N A R R A T O R    D I A L O G
'''
def test_get_dialog_object_connected_narrative_paragraph_model(test_dialog_model):

    sentence_models = etl_wordsum.get_dialog_object_connected_narrative_paragraph_model(test_dialog_model['paragraphStates'][1])

    assert sentence_models[0]['dialogState']['originOfDialogFromOrderParagraph'] == 1
    assert sentence_models[0]['dialogState']['originOfDialogFromOrderParagraph'] == test_dialog_model['paragraphStates'][1]['sentenceStates'][1]['dialogState']['originOfDialogFromOrderParagraph']


def test_get_narrative_with_dialog_object_paragraph_model_first(test_dialog_model):

    sentence_model_narrator = etl_wordsum.get_narrative_with_dialog_object_paragraph_model(test_dialog_model['paragraphStates'][1], 1)

    assert sentence_model_narrator[0]['sentence'] == "Rind shouts, DIALOG_OBJECT_1"



def test_get_narrative_with_dialog_object_paragraph_model_last(test_dialog_model):

    sentence_model_narrator = etl_wordsum.get_narrative_with_dialog_object_paragraph_model(test_dialog_model['paragraphStates'][80], 3)

    assert sentence_model_narrator[0]['sentence'] == "DIALOG_OBJECT_1, says Rind holding arms under cloak and looking at Tommy."
    assert sentence_model_narrator[1]['sentence'] == "I don't know,''"


def test_get_dialog_connected_dialog_object_paragraph_model_last(test_dialog_model):

    sentence_model_dialog = etl_wordsum.get_dialog_connected_dialog_object_paragraph_model(test_dialog_model['paragraphStates'][1], 1)

    print(sentence_model_dialog)

    assert sentence_model_dialog[0]['sentence'] == "Rind shouts, DIALOG_OBJECT_1"