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

from sklearn.manifold import TSNE
import matplotlib.pyplot as plot
import os
import logging
import gensim
import pandas as pd

def get_file_basename(path_file):
    logging.debug("get_file_basename")

    if path_file is not None:
        file = os.path.splitext(path_file)[0]
        file_base = os.path.basename(file)
    else:
        file_base = None

    return file_base


def vector_story_model_plot(path_model, path_save):

    model = gensim.models.Word2Vec.load(path_model)
    vocab = list(model.wv.vocab)
    X = model[vocab]
    tsne = TSNE(n_components=2, random_state=0)
    X_tsne = tsne.fit_transform(X)

    df = pd.concat([pd.DataFrame(X_tsne),
                    pd.Series(vocab)],
                   axis=1)

    df.columns = ['x', 'y', 'word']

    fig = plot.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(df['x'], df['y'])
    for i, txt in enumerate(df['word']):
        ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))

    file_name = get_file_basename(path_model)

    plot.savefig(path_save + file_name + ".svg")

def get_file_list(file):

    file_list = []

    if os.path.isfile(file):
        file_list.append(file)

    if os.path.isdir(file):
        for filename in os.listdir(file):
            if filename.endswith(".json"):
                file_list.append(file + os.path.sep + filename)

    return file_list