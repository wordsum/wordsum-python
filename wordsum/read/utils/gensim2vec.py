import gensim
import logging
import os


PATH_SCRIPT=os.path.dirname(os.path.realpath(__file__))
PATH_TRAIN=os.path.join(PATH_SCRIPT, '../../data/train/')
PATH_MODEL=os.path.join(PATH_SCRIPT, '../../data/model/')



'''
Train the model with lists of lists of sentences.

TODO: either by object or parameters set remaining Word2Vec parameters and check.
'''
def train_sentences(sentences):
    logging.debug("sentences: ", sentences)

    if not sentences is None:
        model = gensim.models.Word2Vec(sentences, min_count=1)
    else:
        print("No sentences")
        model = None

    return model


'''
save the model locally to later use.
'''
def save_model(model, path):

    if not model is None:
        model.save(path)
    else:
        print("No model to save.")

