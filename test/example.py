import gensim
import numpy

# word2vec = gensim.models.KeyedVectors.load_word2vec_format('path-to/GoogleNews-vectors-negative300.bin',binary=True) #google default vectors bin =TRUE
# print('Google-Model: ',word2vec.wv.most_similar_cosmul(positive=['king', 'woman'], negative=['man'], topn=30))


# word2vec = gensim.models.KeyedVectors.load_word2vec_format('C:/tmp_project/WNParser/models/300d-5w-1mc-sg-ns.vector', binary=False) #in case we have the actual vectors in a text file
# word2vec = gensim.models.KeyedVectors.load('C:/tmp_project/WNParser/models/300d-5w-1mc-sg-ns.model')  # binary
word2vec = gensim.models.KeyedVectors.load_word2vec_format(
    '/home/charles/terry_algorithms/GoogleNews/GoogleNews-vectors-negative300.bin', binary=True)
# word2vec = gensim.models.KeyedVectors.load(
#     '/home/charles/terry_algorithms/WikipediaDump_2010/mssa/300d-hs-15w-10mc-cbow.model')


print('word2vec-size:\t', word2vec.vector_size)
# print('Actual Vector: \t', word2vec.word_vec('Charles'))
print('Google-Model: ', word2vec.wv.most_similar_cosmul(positive=['house'], topn=30))
# print('Model-Similar: ', word2vec.wv.most_similar_cosmul(positive=['<positive1>','<positive2>'], negative=['<negative1>'], topn=30))
# print('Model-Similar-Cosmul: ',word2vec.wv.most_similar(positive=['<positive1>','<positive2>'], negative=['<negative1>'], topn=30))
# print('Most Similar: \t', word2vec.wv.most_similar('food.n.01'))

# ===============================================================================
key = 'value'

try:
    po = word2vec.word_vec(key)
except KeyError:
    po = numpy.full(4, 0.01)
    print('word2vec-value:\t', po)
# ===============================================================================
quit()
