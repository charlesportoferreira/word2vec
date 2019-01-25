from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import datapath, get_tmpfile


class Main:

    def main(self):
        a = 2
        print("test")
        glove_file = datapath("test_glove.txt")
        glove_file2 = 'glove.6B.300d.txt'
        tmp_file = get_tmpfile("test_word2vc.txt")
        _ = glove2word2vec(glove_file2, tmp_file)
        model = KeyedVectors.load_word2vec_format(tmp_file)
        print("loaded")
        print(model.word_vec("house"))
        quit()


if __name__ == "__main__":
    Main().main()
