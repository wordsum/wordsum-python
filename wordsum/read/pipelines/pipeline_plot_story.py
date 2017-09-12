'''
Pipeline to plot story per chapter then as an entire book and use the distance of the vector change per chaper plot through
the story.

'''
import wordsum.read.utils.gensim2vec as gensim2vec
import wordsum.read.utils.etl4vec as etl4vec
import logging
import json


def process(file, path_model_dump):
    logging.debug("pipeline_plot_story: Beginning.")

    with open(file) as data_file:
        text_model = json.load(data_file)

    story = etl4vec.get_text_model_narrator_paragraphs(text_model)

    etl4vec.replace_punctuation_story(story)

    return story




