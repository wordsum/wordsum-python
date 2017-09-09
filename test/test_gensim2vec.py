'''
Tests to test gensim.
'''
import wordsum.read.gensim2vec as gensim2vec


def test_train_sentences():

    sentences = [['A', 'beginning'], ['A', 'start']]

    model = gensim2vec.train_sentences(sentences)

    print(model.wv['A'])

    assert  model!=None


