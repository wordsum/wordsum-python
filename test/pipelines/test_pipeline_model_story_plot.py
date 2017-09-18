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

import os
import wordsum.read.pipelines.pipeline_model_story_plot as pipeline_plot_story

TEST_DIR = os.path.realpath('./') + '/data/train/plot/The_Detective_Store'
TEST_FILE = os.path.realpath('./') + '/data/train/plot/The_Detective_Store/0001.json'
TEST_LOCAL_MODEL_DUMP  = os.path.realpath('./') + '/data/models/The_Detective_Store/'


def test_process_file():

    story = pipeline_plot_story.process(TEST_FILE, TEST_LOCAL_MODEL_DUMP)

    #assert ['towel', 'around', 'neck', 'is'] == story[0]


def test_process_dir():

    story = pipeline_plot_story.process(TEST_DIR, TEST_LOCAL_MODEL_DUMP)







