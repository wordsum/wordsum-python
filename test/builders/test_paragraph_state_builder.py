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
import wordsum.read.models.text.paragraph.paragraph_patterns as paragraph_patterns
import wordsum.read.models.text.paragraph.paragraph_state as paragraph_state
import wordsum.read.models.text.paragraph.paragraph_tags as paragraph_tags
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


PARAGRAPH_DIALOG_BEGIN_END = ["''Where are we going?''",
                              "\"I began this string.\"",
                              ",,What are we thinking?''",
                              ">I don't know.<",
                              "<I don't know.>",
                              ">|I don't know.<",
                              "<|I don't know.>"]

PARAGRAPH_END = ["I don't know?",
                 "I don't know!",
                 "I don't know."]

MARK_DIALOG_BEGIN_STRING = ["I don't know? ,,The some dialog.''",
                           "I don't know? ''The some dialog.''",
                           "I don't know? >|The some dialog.<",
                           "I don't know? <|The some dialog.>",
                           "I don't know? <The some dialog.>",
                           "I don't know? >The some dialog.<",
                           "I don't know. ,,The some dialog.''",
                           "I don't know. ''The some dialog.''",
                           "I don't know. >|The some dialog.<",
                           "I don't know. <|The some dialog.>",
                           "I don't know. <The some dialog.>",
                           "I don't know. >The some dialog.<"]


NARRATOR_BEGIN_NARRATOR_END_STRING = ["I say, \"I don't know?\"",
                           "I say, ''The same dialog.''",
                           "I speak, >|The some dialog.<",
                           "I thought, <|The some dialog.>",
                           "I thought, <The some dialog.>",
                           "I speak, >The some dialog.<",
                           "I say, ,,The some dialog.''"]

DIALOG_BEGIN_NARRATOR_END_STRING = ["\"I don't know,\" I say.",
                                      "''The same dialog,'' I say.",
                                      ">|The some dialog,< I speak.",
                                      "<|The some dialog,> I thought.",
                                      "<The some dialog,> I thought."]


def test_set_paragraph():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    state = builder.set_paragraph(state, end, tags, PARAGRAPH_NO_DIALOG)

    assert state.text == PARAGRAPH_NO_DIALOG



def test_split_paragraph_text():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    state = builder.set_paragraph(state, end, tags, PARAGRAPH_NO_DIALOG)
    state = builder.split_paragraph_text(state)

    dict_state = list(state.paragraph_dict.items())

    assert dict_state[0][0] + dict_state[1][0] == "The valley filled with smoke smoldering from pine trees. "


def test_split_paragraph_text_dialog():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    state = builder.set_paragraph(state, end, tags, PARAGRAPH_AUDIO_DIALOG)
    state = builder.split_paragraph_text(state)

    dict_state = list(state.paragraph_dict.items())

    assert dict_state[0][0] + dict_state[1][0] + dict_state[2][0] + dict_state[3][0] == "I said, ,,The time has come to stop.'' "

def test_split_paragraph_text_dialog_split_begin_end():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in PARAGRAPH_DIALOG_BEGIN_END:
        state = builder.set_paragraph(state, end, tags, string)
        state = builder.split_paragraph_text(state)

        dict_state = list(state.paragraph_dict.items())

        i += 1

        assert dict_state[0][0] + dict_state[1][0] +  dict_state[2][0] == PARAGRAPH_DIALOG_BEGIN_END[i]

def test_split_paragraph_text_split_end():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in PARAGRAPH_END:
        state = builder.set_paragraph(state, end, tags, string)
        state = builder.split_paragraph_text(state)

        dict_state = list(state.paragraph_dict.items())

        i += 1

        assert dict_state[0][0] + dict_state[1][0] == PARAGRAPH_END[i]


def test_mark_dialog_begin_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()


    i = -1

    for string in MARK_DIALOG_BEGIN_STRING:
        state = builder.set_paragraph(state, end, tags, string)
        state = builder.split_paragraph_text(state)

        dict_state = list(state.paragraph_dict.items())

        i += 1

        assert dict_state[0][0] + dict_state[1][0] + dict_state[2][0] + dict_state[3][0] + dict_state[4][0] == MARK_DIALOG_BEGIN_STRING[i]


def test_narrative_continue_to_dialog_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in NARRATOR_BEGIN_NARRATOR_END_STRING:
        state = builder.set_paragraph(state, end, tags, string)
        state = builder.split_paragraph_text(state)

        dict_state = list(state.paragraph_dict.items())

        i += 1

        assert dict_state[0][0] + dict_state[1][0] + dict_state[2][0] + dict_state[3][0] == NARRATOR_BEGIN_NARRATOR_END_STRING[i]


def test_dialog_continue_to_narrator_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    end = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in DIALOG_BEGIN_NARRATOR_END_STRING:
        state = builder.set_paragraph(state, end, tags, string)
        state = builder.split_paragraph_text(state)

        dict_state = list(state.paragraph_dict.items())

        i += 1

        assert dict_state[0][0] + dict_state[1][0] + dict_state[2][0] + dict_state[3][0] + dict_state[4][0] == DIALOG_BEGIN_NARRATOR_END_STRING[i]