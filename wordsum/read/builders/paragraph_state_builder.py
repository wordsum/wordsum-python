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
import logging
import regex
import collections
import wordsum.read.builders.sentence_state_builder as sentence_state_builder
import wordsum.read.models.text.sentence.sentence_state as sentence_state
'''
A function to get checck for state and set the two things the object needs to begin.
'''
def set_paragraph(paragraph_state, paragraph_patterns, paragraph_tags, text):
    logging.debug("build_paragraph.")

    if paragraph_state is None or paragraph_patterns is None or text is None:
        logging.info("build_paragraph is ", paragraph_state)
        logging.info("paragraph_end is ", paragraph_patterns)
        logging.info("text is ", text)

    else:

        paragraph_state.paragraph_patterns = paragraph_patterns
        paragraph_state.text = text
        paragraph_state.paragraph_list_dict = []
        paragraph_state.paragraph_tags = paragraph_tags

    return paragraph_state

'''
A function that will split the paragraph by punctuation and put both in an array to later be used to define the words.
'''
def split_paragraph_text(paragraph_state):
    logging.debug("split_paragraph_text")

    if paragraph_state.text is None or paragraph_state.paragraph_patterns is None or paragraph_state.paragraph_tags is None:
        logging.info("split_paragraph_text: Returning paragraph_state unaltered because no text, tags or paragraph_patterns object found.")
    else:

        regex_return = regex.compile(paragraph_state.paragraph_patterns.split)
        # Split into list
        paragraph_array = regex_return.split(paragraph_state.text)
        # Remove the empty
        paragraph_array[:] = [item for item in paragraph_array if item != '']
        # Set into list of ordered dicts to save position.
        for i,string in enumerate(paragraph_array):
            paragraph_state.paragraph_list_dict.append(collections.OrderedDict([(string, paragraph_state.paragraph_tags.no_tag)]))


    return paragraph_state

'''
A function to define the punctuation, dialog and narrative objects.
'''
def tag_paragraph_list_dict_data(paragraph_state):
    logging.debug("create_sentence_states")

    if paragraph_state.paragraph_list_dict is None or \
                    paragraph_state.paragraph_list_dict is False or \
                    paragraph_state.paragraph_tags is None or \
                    paragraph_state.paragraph_patterns is None:

        logging.info("paragraph_state.paragraph_list_dict: " + str(paragraph_state.paragraph_list_dict))
        logging.info("paragraph_state.paragraph_patterns: " + str(paragraph_state.paragraph_patterns))
        logging.info("paragraph_state.paragraph_tags: " + str(paragraph_state.paragraph_tags))
        logging.info("paragraph_state.paragraph_list_dict or paragraph_state.paragraph_patterns is None or False." + str(paragraph_state.paragraph_list_dict))
    else:
        logging.debug("tag_paragraph_list_dict_data: paragraph_state.paragraph_list_dict is " + str(paragraph_state.paragraph_list_dict))


        match_begin_dialog = regex.compile('('+ paragraph_state.paragraph_patterns.dialog_beginning_mark + "|" +
                                           paragraph_state.paragraph_patterns.dialog_mark_begin + ')')


        match_dialog_continuing_mark_to_narrator = regex.compile('(' + paragraph_state.paragraph_patterns.dialog_continuing_mark_to_narrator + ')')


        match_end_dialog = regex.compile('('+ paragraph_state.paragraph_patterns.dialog_ending_mark + "|" +
                                         paragraph_state.paragraph_patterns.dialog_mark_end + ')')

        match_narrator_continuing_mark_to_dialog = regex.compile('(' + paragraph_state.paragraph_patterns.narrator_continuing_mark_to_dialog + ')')

        match_end_narrator = regex.compile('('+ paragraph_state.paragraph_patterns.narrator_ending_mark + ')')

        # Default to narrator because we will know if it is dialog by the mark.
        current_word_tag = paragraph_state.paragraph_tags.narrative

        base_tag = {}

        base_list = []

        enumerate_value = 1

        for ordered_loop_dict in paragraph_state.paragraph_list_dict:

            for key,value in ordered_loop_dict.items():

                #paragraph_state.paragraph_tags.base +   + str(enumerate_value)

                ordered_dict =  collections.OrderedDict()

                if match_begin_dialog.match(key):

                    ordered_dict[key] = paragraph_state.paragraph_tags.syntax  + str(enumerate_value)

                    base_list.append(ordered_dict)

                    current_word_tag = paragraph_state.paragraph_tags.dialog

                elif match_dialog_continuing_mark_to_narrator.match(key):

                    ordered_dict[key] = paragraph_state.paragraph_tags.syntax + str(enumerate_value)

                    base_list.append(ordered_dict)

                    current_word_tag = paragraph_state.paragraph_tags.narrative

                elif match_end_dialog.match(key):

                    ordered_dict[key] = paragraph_state.paragraph_tags.syntax + str(enumerate_value)

                    base_list.append(ordered_dict)

                    base_tag[paragraph_state._paragraph_tags.base + str(enumerate_value)] = base_list

                    base_list = []

                    enumerate_value = enumerate_value + 1

                    current_word_tag = paragraph_state.paragraph_tags.narrative

                elif match_narrator_continuing_mark_to_dialog.match(key):

                    ordered_dict[key] = paragraph_state.paragraph_tags.syntax  + str(enumerate_value)

                    base_list.append(ordered_dict)

                    current_word_tag = paragraph_state.paragraph_tags.dialog

                elif match_end_narrator.match(key):

                    ordered_dict[key] = paragraph_state.paragraph_tags.syntax + str(enumerate_value)

                    base_list.append(ordered_dict)

                    base_tag[paragraph_state._paragraph_tags.base + str(enumerate_value)] = base_list

                    base_list = []

                    enumerate_value = enumerate_value + 1

                else:

                    ordered_dict[key] = current_word_tag + str(enumerate_value)

                    base_list.append(ordered_dict)

        paragraph_state.paragraph_list_dict = base_tag

    return paragraph_state

'''
A function to create the sentence_list_dicts with dialog marks.

this function needs to work to separate dialog from narrative in sentences where they are both.
 Then it will make the the sentence states.

 This is one wayy of making sentence states from the array above. I may move the logic that creates the states.

'''
def create_sentence_states(paragraph_state):
    logging.debug("create_sentence_states")

    if paragraph_state.paragraph_list_dict is None or paragraph_state.paragraph_list_dict is False:
        logging.info("tag_paragraph_list_dict_data: paragraph_state.paragraph_list_dict or paragraph_state.paragraph_patterns is None or False." + str(paragraph_state.paragraph_list_dict))
    else:
        logging.debug("tag_paragraph_list_dict_data: paragraph_state.paragraph_list_dict is " + str(paragraph_state.paragraph_list_dict))

        match_begin = regex.compile('('+ paragraph_state.paragraph_patterns.dialog_beginning_mark + "|" +
                                           paragraph_state.paragraph_patterns.dialog_mark_begin + ')')

        match_end = regex.compile('('+ paragraph_state.paragraph_patterns.dialog_ending_mark + "|" +
                                         paragraph_state.paragraph_patterns.dialog_mark_end +
                                         paragraph_state.paragraph_patterns.narrator_ending_mark + ')')

        match_dialog_continuing_to_narrator = regex.compile('(' + paragraph_state.paragraph_patterns.dialog_continuing_mark_to_narrator + ')')
        match_narrator_continuing_to_dialog = regex.compile('(' + paragraph_state.paragraph_patterns.narrator_continuing_mark_to_dialog + ')')


        sentence_states = []

        regex_punct = regex.compile(paragraph_state.paragraph_tags.syntax + "*")
        regex_dialog = regex.compile(paragraph_state.paragraph_tags.dialog + "*")
        regex_narrator = regex.compile(paragraph_state.paragraph_tags.narrative + "*")

        for key, array in paragraph_state.paragraph_list_dict.items():

            sentence_list_dict = []
            item_i = 0

            for item in array:

                for text, tag in item.items():

                    item_i = item_i + 1

                    # Use the marks to determine and find the narrative object to add  some dialog object.
                    if regex_punct.match(tag):

                        if regex.match(match_begin, text):
                            sentence_list_dict.append({text,tag})

                        if regex.match(match_end, text):
                            sentence_list_dict.append({text,tag})

                        if regex.match(match_dialog_continuing_to_narrator, text):
                            sentence_list_dict.append({text,tag})
                            item.items(item_i)

                            state = sentence_state.Sentence_State()
                            state.text_list_dict = sentence_list_dict
                            sentence_states.append(state)

                        if regex.match(match_narrator_continuing_to_dialog, text):
                            sentence_states.append(state)
                            state = sentence_state.Sentence_State()
                            sentence_list_dict.append({text,tag})


                    elif regex_narrator.match(tag):
                        sentence_list_dict.append({text,tag})
                    elif regex_dialog.match(tag):
                        sentence_list_dict.append({text,tag})

            state = sentence_state.Sentence_State()
            state.text_list_dict = sentence_list_dict
            sentence_states.append(state)


        return sentence_states

