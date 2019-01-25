import gensim
import numpy
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import get_tmpfile


class Word2VectorUtil:
    model = None
    simulation = False
    aggregator = "sum"
    simulation_value = 1
    model_path = None
    number_features = 0
    type = None

    def __init__(self, aggregator, model_path, type='mssa', simulation=False, simulation_value=1):
        self.simulation = simulation
        self.aggregator = aggregator
        self.simulation_value = simulation_value
        self.model_path = model_path
        self.type = type
        if not self.simulation:
            print("loading w2v model...")
            self.model = self.load_model()
            print('done!\nword2vec-size:\t', self.model.vector_size)
            self.number_features = self.model.vector_size

    def load_model(self):
        if self.type == "google":
            return gensim.models.KeyedVectors.load_word2vec_format(self.model_path, binary=True)
        elif self.type == 'mssa':
            return gensim.models.KeyedVectors.load(self.model_path)
        elif self.type == "glove":
            return self.get_glove()
        raise "\n\nwrong model type: " + self.type

    def get_glove(self):
        glove_file = self.model_path
        tmp_file = get_tmpfile("test_word2vc.txt")
        _ = glove2word2vec(glove_file, tmp_file)
        return KeyedVectors.load_word2vec_format(tmp_file)

    def word2vec_simulation(self, value):
        return numpy.full(4, value)

    def get_list_vectors(self, tokens):
        list_vec = []
        for token in tokens:
            if self.simulation:
                list_vec.append(self.word2vec_simulation(self.simulation_value))
            else:
                try:
                    list_vec.append(self.model.word_vec(token))
                    # print("vector found <" + token+ ">")
                except KeyError:
                    # print("vector not found: <" + token + ">")  # do nothing
                    continue
        return list_vec

    def get_doc_vector(self, tokens):
        list_vec = self.get_list_vectors(tokens)
        if len(list_vec) == 0:
            return []  # no vector found

        if self.aggregator == "sum":
            return numpy.sum(list_vec, axis=0)

        if self.aggregator == "mean":
            return numpy.mean(list_vec, axis=0)

        raise "wrong aggregator: " + self.aggregator
