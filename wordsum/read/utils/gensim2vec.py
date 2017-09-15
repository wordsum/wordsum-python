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

import gensim
import logging


'''
Train the model with lists of lists of sentences.

TODO: either by object or parameters set remaining Word2Vec parameters and check.
'''
def train_sentences(sentences):
    logging.debug("sentences: ", sentences)

    if not sentences is None:
        model = gensim.models.Word2Vec(sentences, size=10, window=5, min_count=5, workers=4)
    else:
        print("No sentences")
        model = None

    return model


'''
save the model locally to later use.
'''
def save_model_binary(model, path, file):

    if not model is None:
        model.save(path + file + ".bin")
    else:
        print("No model to save.")


'''
save the model to text file.
'''
def save_model_text(model, path, file):

    if not model is None:
        model.wv.save_word2vec_format(fname=path + "/" + file + ".txt", fvocab=None, binary=False)
    else:
        print("No model to save.")

