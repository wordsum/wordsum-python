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
# and if another writer writes or edits the Story then the writer's name needs to be apppatternsed to the patterns of the Writer list of this Open Story License.

'''
import wordsum.read.models.text.paragraph.paragraph_patterns as paragraph_patterns
import wordsum.read.models.text.paragraph.paragraph_state as paragraph_state
import wordsum.read.models.text.paragraph.paragraph_tags as paragraph_tags
import wordsum.read.builders.paragraph_state_builder as builder
import collections

PARAGRAPH_NO_DIALOG = str("The valley filled with smoke smoldering from pine trees."
                          " She teleported from the mountain!"
                        " The wordless shout echoes from Sue."
                        " Does she smell like smoke?"
                        " Only her nose knows.")

PARAGRAPH_REPEAT_patternsING = str("I wake. I stand. I code. I lay. I sleep.")

PARAGRAPH_AUDIO_DIALOG = str(",,What.'' I said, ,,The time has come to stop!'' Then I ran for the lake. The killer bees were chasing as I was shouting, ''RUN, SUE!''"
                            " Sue heard. Sue looked back. ,,What?'' She breathed and thought, <Run. Run fast.>"
                            " I thought to her, >I will miss you.< And I dived into the river. >|I will never forget.<")

PARAGRAPHS_CONTINUE_DIALOG = str("She sat before the computer and thought, <I have wrote this before,> while saying to John, ,,I can help you,'' then stood and throught, <I need a more challenging job.")


PARAGRAPH_DIALOG_BEGIN_patterns = ["''Where are we going?''",
                              "\"I began this string.\"",
                              ",,What are we thinking?''",
                              ">I don't know.<",
                              "<I don't know.>",
                              ">|I don't know.<",
                              "<|I don't know.>"]

PARAGRAPH_patterns = ["I don't know?",
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


NARRATOR_BEGIN_NARRATOR_patterns_STRING = ["I say, \"I don't know?\"",
                           "I say, ''The same dialog.''",
                           "I speak, >|The some dialog.<",
                           "I thought, <|The some dialog.>",
                           "I thought, <The some dialog.>",
                           "I speak, >The some dialog.<",
                           "I say, ,,The some dialog.''"]

DIALOG_BEGIN_NARRATOR_patterns_STRING = ["\"I don't know,\" I say.",
                                      "''The same dialog,'' I say.",
                                      ">|The some dialog,< I speak.",
                                      "<|The some dialog,> I thought.",
                                      "<The some dialog,> I thought."]


PARAGRAPH_TAGGED = [collections.OrderedDict([(',,', 'PUNCTUATION_OBJECT_1')]),
                    collections.OrderedDict([('What', 'DIALOG_OBJECT_1')]),
                    collections.OrderedDict([(".'' ", 'PUNCTUATION_OBJECT_1')]),

                    collections.OrderedDict([('I said', 'NARRATIVE_OBJECT_2')]),
                    collections.OrderedDict([(', ,,', 'PUNCTUATION_OBJECT_2')]),
                    collections.OrderedDict([('The time has come to stop', 'DIALOG_OBJECT_2')]),
                    collections.OrderedDict([("!'' ", 'PUNCTUATION_OBJECT_2')]),

                    collections.OrderedDict([('Then I ran for the lake', 'NARRATIVE_OBJECT_3')]),
                    collections.OrderedDict([('. ', 'PUNCTUATION_OBJECT_3')]),

                    collections.OrderedDict([('The killer bees were chasing as I was shouting', 'NARRATIVE_OBJECT_4')]),
                    collections.OrderedDict([(", ''", 'PUNCTUATION_OBJECT_4')]),
                    collections.OrderedDict([('RUN, SUE', 'DIALOG_OBJECT_4')]),
                    collections.OrderedDict([("!'' ", 'PUNCTUATION_OBJECT_4')]),

                    collections.OrderedDict([('Sue heard', 'NARRATIVE_OBJECT_5')]),
                    collections.OrderedDict([('. ', 'PUNCTUATION_OBJECT_5')]),

                    collections.OrderedDict([('Sue looked back', 'NARRATIVE_OBJECT_6')]),
                    collections.OrderedDict([('. ', 'PUNCTUATION_OBJECT_6')]),

                    collections.OrderedDict([(',,', 'PUNCTUATION_OBJECT_7')]),
                    collections.OrderedDict([('What', 'DIALOG_OBJECT_7')]),
                    collections.OrderedDict([("?'' ", 'PUNCTUATION_OBJECT_7')]),

                    collections.OrderedDict([('She breathed and thought', 'NARRATIVE_OBJECT_8')]),
                    collections.OrderedDict([(', <', 'PUNCTUATION_OBJECT_8')]),
                    collections.OrderedDict([('Run', 'DIALOG_OBJECT_8')]),
                    collections.OrderedDict([('. ', 'PUNCTUATION_OBJECT_8')]),

                    collections.OrderedDict([('Run fast', 'DIALOG_OBJECT_9')]),
                    collections.OrderedDict([('.> ', 'PUNCTUATION_OBJECT_9')]),

                    collections.OrderedDict([('I thought to her', 'NARRATIVE_OBJECT_10')]),
                    collections.OrderedDict([(', >', 'PUNCTUATION_OBJECT_10')]),
                    collections.OrderedDict([('I will miss you', 'DIALOG_OBJECT_10')]),
                    collections.OrderedDict([('.< ', 'PUNCTUATION_OBJECT_10')]),

                    collections.OrderedDict([('And I dived into the river', 'NARRATIVE_OBJECT_11')]),
                    collections.OrderedDict([('. ', 'PUNCTUATION_OBJECT_11')]),

                    collections.OrderedDict([('>|', 'PUNCTUATION_OBJECT_12')]),
                    collections.OrderedDict([('I will never forget', 'DIALOG_OBJECT_12')]),
                    collections.OrderedDict([('.<', 'PUNCTUATION_OBJECT_12')])]


PARAGRAPH_TAGGED_LIST = [{'OBJECT_1':  (collections.OrderedDict([(',,', 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('What', 'DIALOG_OBJECT_1')]),
                                        collections.OrderedDict([(".'' ", 'PUNCTUATION_OBJECT_1')]))},

                         {'OBJECT_2':  (collections.OrderedDict([('I said', 'NARRATIVE_OBJECT_2')]),
                                        collections.OrderedDict([(', ,,', 'PUNCTUATION_OBJECT_2')]),
                                        collections.OrderedDict([('The time has come to stop', 'DIALOG_OBJECT_2')]),
                                        collections.OrderedDict([("!'' ", 'PUNCTUATION_OBJECT_2')]))}]

PARAGRAPHS_CONTINUE_DIALOG_LIST_DICT = [collections.OrderedDict([('She sat before the computer and thought', 'NARRATIVE_OBJECT_1')]),
                                        collections.OrderedDict([(', <', 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('I have wrote this before', 'DIALOG_OBJECT_1')]),
                                        collections.OrderedDict([(',> ', 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('while saying to John', 'NARRATIVE_OBJECT_1')]),
                                        collections.OrderedDict([(', ,,', 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('I can help you', 'DIALOG_OBJECT_1')]),
                                        collections.OrderedDict([(",'' ", 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('then stood and throught', 'NARRATIVE_OBJECT_1')]),
                                        collections.OrderedDict([(', <', 'PUNCTUATION_OBJECT_1')]),
                                        collections.OrderedDict([('I need a more challenging job', 'DIALOG_OBJECT_1')]),
                                        collections.OrderedDict([('.', 'PUNCTUATION_OBJECT_1')])]


def test_set_paragraph():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_NO_DIALOG)

    assert state.text == PARAGRAPH_NO_DIALOG

def test_set_split_paragraph_same_patternsing_and_capture():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_REPEAT_patternsING)

    builder.split_paragraph_text(state)

    assert state.text == PARAGRAPH_REPEAT_patternsING

def test_split_paragraph_text():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_NO_DIALOG)
    builder.split_paragraph_text(state)

    assert list(state.paragraph_list_dict[0].items())[0][0] + \
           list(state.paragraph_list_dict[1].items())[0][0]  == "The valley filled with smoke smoldering from pine trees. "


def test_split_paragraph_text_dialog():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_AUDIO_DIALOG)
    builder.split_paragraph_text(state)


    assert  list(state.paragraph_list_dict[0].items())[0][0] + \
            list(state.paragraph_list_dict[1].items())[0][0] + \
            list(state.paragraph_list_dict[2].items())[0][0] + \
            list(state.paragraph_list_dict[3].items())[0][0] == ",,What.'' I said"

def test_split_paragraph_text_dialog_split_begin_patterns():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in PARAGRAPH_DIALOG_BEGIN_patterns:
        builder.set_paragraph(state, patterns, tags, string)
        builder.split_paragraph_text(state)

        i += 1

        assert list(state.paragraph_list_dict[0].items())[0][0] + \
               list(state.paragraph_list_dict[1].items())[0][0] + \
               list(state.paragraph_list_dict[2].items())[0][0] == PARAGRAPH_DIALOG_BEGIN_patterns[i]

def test_split_paragraph_text_split_patterns():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in PARAGRAPH_patterns:
        builder.set_paragraph(state, patterns, tags, string)
        builder.split_paragraph_text(state)


        i += 1

        assert list(state.paragraph_list_dict[0].items())[0][0] + \
               list(state.paragraph_list_dict[1].items())[0][0] == PARAGRAPH_patterns[i]


def test_mark_dialog_begin_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()


    i = -1

    for string in MARK_DIALOG_BEGIN_STRING:
        builder.set_paragraph(state, patterns, tags, string)
        builder.split_paragraph_text(state)

        i += 1

        assert list(state.paragraph_list_dict[0].items())[0][0] + \
               list(state.paragraph_list_dict[1].items())[0][0] + \
               list(state.paragraph_list_dict[2].items())[0][0] + \
               list(state.paragraph_list_dict[3].items())[0][0] + \
               list(state.paragraph_list_dict[4].items())[0][0] == MARK_DIALOG_BEGIN_STRING[i]


def test_narrative_continue_to_dialog_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in NARRATOR_BEGIN_NARRATOR_patterns_STRING:
        builder.set_paragraph(state, patterns, tags, string)
        builder.split_paragraph_text(state)

        i += 1

        assert list(state.paragraph_list_dict[0].items())[0][0] + \
               list(state.paragraph_list_dict[1].items())[0][0] + \
               list(state.paragraph_list_dict[2].items())[0][0] + \
               list(state.paragraph_list_dict[3].items())[0][0] == NARRATOR_BEGIN_NARRATOR_patterns_STRING[i]


def test_dialog_continue_to_narrator_string():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    i = -1

    for string in DIALOG_BEGIN_NARRATOR_patterns_STRING:
        builder.set_paragraph(state, patterns, tags, string)
        builder.split_paragraph_text(state)

        i += 1

        assert list(state.paragraph_list_dict[0].items())[0][0] + \
               list(state.paragraph_list_dict[1].items())[0][0] + \
               list(state.paragraph_list_dict[2].items())[0][0] + \
               list(state.paragraph_list_dict[3].items())[0][0] + \
               list(state.paragraph_list_dict[4].items())[0][0] == DIALOG_BEGIN_NARRATOR_patterns_STRING[i]


'''
T A G G I N G
'''
def test_none_paragraph_tag_in_paragraph_state_in_split_paragraph():

    state = paragraph_state.Paragraph_State()
    tags = None
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_NO_DIALOG)
    builder.split_paragraph_text(state)

    assert state.paragraph_list_dict == []

def test_enumerate_tag_paragraph_list_dict_data():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPH_AUDIO_DIALOG)
    builder.split_paragraph_text(state)
    builder.tag_paragraph_list_dict_data(state)

    assert PARAGRAPH_TAGGED == state.paragraph_list_dict

def test_enumerate_tag_paragraph_list_dict_data_nested_dialog():

    state = paragraph_state.Paragraph_State()
    tags = paragraph_tags.Paragraph_Tags()
    patterns = paragraph_patterns.Paragraph_Patterns()

    builder.set_paragraph(state, patterns, tags, PARAGRAPHS_CONTINUE_DIALOG)
    builder.split_paragraph_text(state)
    builder.tag_paragraph_list_dict_data(state)

    assert PARAGRAPHS_CONTINUE_DIALOG_LIST_DICT == state.paragraph_list_dict


def test_create_sentence_states_dialog_begin():

    state = paragraph_state.Paragraph_State()
    state.paragraph_list_dict = PARAGRAPH_TAGGED

    builder.create_sentence_states(state)



    assert PARAGRAPHS_CONTINUE_DIALOG_LIST_DICT == state.paragraph_list_dict