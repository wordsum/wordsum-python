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

import wordsum.read.pipelines.utilities as utilities
import os

def test_get_file_basename():

    file_basename = utilities.get_file_basename("/home/tester/path/file.txt")

    assert file_basename == "file"


def test_vector_story_model_plot():

    path_model = os.path.realpath('./') + '/data/models/0001.bin'

    utilities.vector_story_model_plot(path_model)