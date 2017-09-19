import json
import wordsum.read.utils.etl_wordsum as etl_wordsum


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
