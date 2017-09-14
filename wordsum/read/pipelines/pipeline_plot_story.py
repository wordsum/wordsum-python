'''
Pipeline to plot story per chapter then as an entire book and use the distance of the vector change per chaper plot through
the story.

'''
import wordsum.read.utils.gensim2vec as gensim2vec
import wordsum.read.utils.etl4vec as etl4vec
import logging
import json
import os
import wordsum.read.pipelines.utilities as utilities


PATH_SCRIPT=os.path.dirname(os.path.realpath(__file__))


def process(file, path_model_dump):
    logging.debug("pipeline_plot_story: Beginning.")

    # Open wordsum file.
    with open(file) as data_file:
        text_model = json.load(data_file)

    # Get only the narrator sentences and leave the dialog.
    story = etl4vec.get_text_model_narrator_paragraphs(text_model)

    # Replace punctuation, so we can group words.
    etl4vec.replace_punctuation_story(story)

    # Vector sentences of story now that we have removed punctuations.
    # This is done after the remove of punctuation like spaces with the em dash.
    etl4vec.list_sentences_in_story(story)

    # Reduce the lists of lists to a list of lists.
    story_list = etl4vec.list_story_lists(story)

    # Get the origin file.
    file_basename = utilities.get_file_basename(file)

    # Create the model.
    model = gensim2vec.train_sentences(story_list)

    # Save the model to binary.
    gensim2vec.save_model_binary(model, path_model_dump, file_basename)

    #  Save the text version.
    gensim2vec.save_model_text(model, path_model_dump, file_basename)

    return story_list




