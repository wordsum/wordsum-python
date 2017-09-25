'''
# Open Story License
#
# Story: wordsum-python
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

'''
import wordsum.read.models.text.sentence.sentence_end as sentence_end
import wordsum.read.models.text.paragraph.paragraph_state as paragraph_state
import wordsum.read.builders.paragraph_state_builder as builder

PARAGRAPH_NO_DIALOG = str("The valley filled with smoke smoldering from pine trees."
                          " She teleported from the mountain!"
                        " The wordless shout echoes from Sue."
                        " Does she smell like smoke?"
                        " Only her nose knows.")

PARAGRAPH_AUDIO_DIALOG = str("I said, ,,The time has come to stop.''"
                            " Then I ran for the lake. The killer bees were chasing as I was shouting, ''RUN, SUE!''"
                            " Sue heard. Sue looked back. ,,What?'' She breathed and thought, <Run. Run fast.>"
                            " I thought to her, >I will miss you.< And I dived into the river. >|I will never forget.<")

def test_set_paragraph():

    state = paragraph_state.Paragraph_State()
    end = sentence_end.Sentence_End()

    state = builder.set_paragraph(state, end, PARAGRAPH_NO_DIALOG)

    assert state.text == PARAGRAPH_NO_DIALOG



def test_split_paragraph_text():

    state = paragraph_state.Paragraph_State()
    end = sentence_end.Sentence_End()

    state = builder.set_paragraph(state, end, PARAGRAPH_NO_DIALOG)
    sentences = builder.split_paragraph_text(state)

    assert sentences[0] + sentences[1] == "The valley filled with smoke smoldering from pine trees. "


def test_split_paragraph_text_dialog():

    state = paragraph_state.Paragraph_State()
    end = sentence_end.Sentence_End()

    state = builder.set_paragraph(state, end, PARAGRAPH_AUDIO_DIALOG)
    sentences = builder.split_paragraph_text(state)

    assert sentences[0] + sentences[1] + sentences[2] + sentences[3] == "I said, ,,The time has come to stop.'' "