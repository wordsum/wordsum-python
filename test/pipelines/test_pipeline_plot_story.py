import pytest
import json
import os
import wordsum.read.pipelines.pipeline_plot_story as pipeline_plot_story

TEST_FILE = os.path.realpath('./') + '/data/train/plot/0001.json'
TEST_LOCAL_MODEL_DUMP  = os.path.realpath('./') + '/data/models/'


def test_process():

    story = pipeline_plot_story.process(TEST_FILE, TEST_LOCAL_MODEL_DUMP)

    assert ['towel', 'around', 'neck', 'is'] == story[0]






