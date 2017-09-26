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
import re

'''
A function to get checck for state and set the two things the object needs to begin.
'''
def set_paragraph(paragraph_state, sentence_end, text):
    logging.debug("build_paragraph.")

    if paragraph_state is None or sentence_end is None or text is None:
        logging.info("build_paragraph is ", paragraph_state)
        logging.info("paragraph_end is ", sentence_end)
        logging.info("text is ", text)

    else:

        paragraph_state.sentence_end = sentence_end
        paragraph_state.text = text

    return paragraph_state

'''
A function that will split the paragraph by punctuation and put both in an array to later be used to define the words.
'''
def split_paragraph_text(paragraph_state):
    logging.debug("split_paragraph into sentences.")

    if paragraph_state.text is None or paragraph_state.sentence_end is None:
        logging.info("exiting split_paragraph because not text or sentence_end object found.")
        exit()
    else:

        regex = re.compile(paragraph_state.sentence_end.pattern)
        # Split into list
        paragraph_array = regex.split(paragraph_state.text)
        # Remove the empty
        paragraph_array[:] = [item for item in paragraph_array if item != '']
        # Set the array
        paragraph_state.paragraph_array = paragraph_array

    return paragraph_state


