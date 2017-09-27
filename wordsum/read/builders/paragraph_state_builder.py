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
from collections import OrderedDict
import logging
import re
import collections
'''
A function to get checck for state and set the two things the object needs to begin.
'''
def set_paragraph(paragraph_state, paragraph_pattern, paragraph_tags, text):
    logging.debug("build_paragraph.")

    if paragraph_state is None or paragraph_pattern is None or text is None:
        logging.info("build_paragraph is ", paragraph_state)
        logging.info("paragraph_end is ", paragraph_pattern)
        logging.info("text is ", text)

    else:

        paragraph_state.paragraph_pattern = paragraph_pattern
        paragraph_state.text = text
        paragraph_state.paragraph_dict = collections.OrderedDict()
        paragraph_state.paragraph_tags = paragraph_tags

    return paragraph_state

'''
A function that will split the paragraph by punctuation and put both in an array to later be used to define the words.
'''
def split_paragraph_text(paragraph_state):
    logging.debug("split_paragraph_text")

    if paragraph_state.text is None or paragraph_state.paragraph_pattern is None or paragraph_state.paragraph_tags is None:
        logging.info("split_paragraph_text: Returning paragraph_state unaltered because no text, tags or paragraph_pattern object found.")
    else:

        regex = re.compile(paragraph_state.paragraph_pattern.split)
        # Split into list
        paragraph_array = regex.split(paragraph_state.text)
        # Remove the empty
        paragraph_array[:] = [item for item in paragraph_array if item != '']
        # Set into dict
        for i,string in enumerate(paragraph_array):
            paragraph_state.paragraph_dict.update({string: paragraph_state.paragraph_tags.no_tag})

    return paragraph_state

'''
A function to define the punctuation, dialog and narrative objects.
'''
def tag_paragraph_dict_data(paragraph_state):
    logging.debug("tag_paragraph_dict_data")

    if paragraph_state.paragraph_dict is None or paragraph_state.paragraph_dict is False:
        logging.info("tag_paragraph_dict_data: paragraph_state.paragraph_dict is " + paragraph_state.paragraph_dict)
    else:
        logging.debug("tag_paragraph_dict_data: paragraph_state.paragraph_dict is " + paragraph_state.paragraph_dict)



    return paragraph_state
