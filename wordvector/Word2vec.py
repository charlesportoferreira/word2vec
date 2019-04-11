import gensim
import numpy
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import get_tmpfile
import tensorflow as tf
import tensorflow_hub as hub


class Word2VectorUtil:
    model = None
    simulation = False
    aggregator = "mean"
    simulation_value = 1
    model_path = None
    number_features = 0
    type = None

    def __init__(self, aggregator, model_path, model_type='model', simulation=False, simulation_value=1):
        self.simulation = simulation
        self.aggregator = aggregator
        self.simulation_value = simulation_value
        self.model_path = model_path
        self.type = model_type
        if not self.simulation:
            print("loading w2v model...")
            self.model = self.load_model()
            print('done!\nword2vec-size:\t', self.get_number_features())
            self.number_features = self.get_number_features()

    def get_number_features(self):
        if self.type == "elmo":
            return 1024  # TODO: get proper number of features from Elmo
        elif self.type == "use":
            return 512  # TODO: get proper number of features from use
        else:
            return self.model.vector_size

    def load_model(self):
        if self.type == "google":
            return self.get_google_model()
        elif self.type == 'mssa':
            return self.get_mssa_model()
        elif self.type == "glove":
            return self.get_glove_model()
        elif self.type == "fasttext":
            return self.get_fasttest_model()
        elif self.type == "elmo":
            return self.get_elmo_model()
        elif self.type == "use":
            return self.get_use_model()
        elif self.type == "doc2vec":
            return self.get_doc2vec()
        raise "\n\nwrong model type: " + self.type

    def get_doc2vec(self):
        return gensim.models.Doc2Vec.load(self.model_path)

    def get_fasttest_model(self):
        return KeyedVectors.load_word2vec_format(self.model_path, binary=False)

    def get_mssa_model(self):
        return gensim.models.KeyedVectors.load(self.model_path)

    def get_google_model(self):
        return gensim.models.KeyedVectors.load_word2vec_format(self.model_path, binary=True)

    def get_glove_model(self):
        glove_file = self.model_path
        tmp_file = get_tmpfile("test_word2vc.txt")
        _ = glove2word2vec(glove_file, tmp_file)
        return KeyedVectors.load_word2vec_format(tmp_file)

    def get_elmo_model(self):
        model_path = 'https://tfhub.dev/google/elmo/2'
        return self.get_tensorflow_model(model_path)

    def get_use_model(self):
        model_path = "https://tfhub.dev/google/universal-sentence-encoder-large/3"  # newer module
        return self.get_tensorflow_model(model_path)

    def get_tensorflow_model(self, model_path):
        with tf.Graph().as_default():
            sentences = tf.placeholder(tf.string)
            embed = hub.Module(model_path)
            embeddings = embed(sentences)
            session = tf.train.MonitoredSession()
        return lambda x: session.run(embeddings, {sentences: x})

    def word2vec_simulation(self, value):
        return numpy.full(4, value)

    def get_list_vectors(self, tokens):
        if self.type == "elmo":
            return self.get_tensorflow_vectors(tokens)

        if self.type == "use":
            return self.get_tensorflow_vectors(tokens)

        return self.get_gensim_vectors(tokens)

    def get_gensim_vectors(self, tokens):
        list_vec = []
        for token in tokens:
            if self.simulation:
                list_vec.append(self.word2vec_simulation(self.simulation_value))
            else:
                try:
                    list_vec.append(self.model.word_vec(token))
                    # print("vector found <" + token+ ">")
                except KeyError:
                    # print("vector not found: <" + token + ">")
                    continue  # do nothing
        return list_vec

    def get_tensorflow_vectors(self, tokens):
        return self.model(tokens)

    def get_doc_vector(self, tokens):
        list_vec = self.get_list_vectors(tokens)
        if len(list_vec) == 0:
            return []  # no vector found

        if self.aggregator == "sum":
            return numpy.sum(list_vec, axis=0)

        if self.aggregator == "mean":
            return numpy.mean(list_vec, axis=0)

        raise "wrong aggregator: " + self.aggregator
