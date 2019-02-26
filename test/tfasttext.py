import gensim
import io

import numpy
from gensim.models import FastText as ftext
from gensim.models.keyedvectors import KeyedVectors


def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    return data


#
#
# inmodel = '/home/charles/PycharmProjects/w2v/test/wiki.en.bin'
# ftext.load(inmodel)
# load_vectors(inmodel)
# # KeyedVectors.load_word2vec_format
# model = KeyedVectors.load_word2vec_format(inmodel, binary=True)
# # model = KeyedVectors.load(inmodel)
# print(model['house'])
#
# quit()

inmodel = '/home/charles/PycharmProjects/w2v/test/wiki.en.vec'
# ftext.load(inmodel)
# load_vectors(inmodel)
# KeyedVectors.load_word2vec_format
model = KeyedVectors.load_word2vec_format(inmodel, binary=False)
# model = KeyedVectors.load(inmodel)
print(model['house'])
print("********************************************************")
print(model['charles'])
