import gensim
import smart_open
import os.path
import pandas as pd
from gensim.parsing.preprocessing import remove_stopwords

from PreprocessUtil import Preprocess


def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="utf-8", errors="ignore") as f:
        # if tokens are not parsed gensim.utils.simple_preprocess should be used
        # our synsets use word#offset#POS, so they would clean our keys
        # In that case we just tokenize the string read
        for i, line in enumerate(f):
            if tokens_only:  # case for test-token-documents
                yield line.split()
                # yield gensim.utils.simple_preprocess(line)
            else:  # tranining documents must have a TAG-ID, we use INTEGERS.Count
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(line.split(), [i])
                # gives a TAG (int - ID) to every document in fname
                # returns a list of objects TaggedDocument -> ([List of tokens],tag_ID)

                # yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])


print("loading model")
model = gensim.models.Doc2Vec.load("C:/tmp/d2v-raw-words/wd10_raw_d2v.model")
print("model loaded")

my_df = pd.DataFrame()
inferred_vector_list = []

rootpath= os.path.abspath("C:/Users/wgrosky/Desktop/mach")
#rootpath= os.path.abspath("C:/Users/wgrosky/PycharmProjects/task_A/words_dataset")

filenames = os.listdir(rootpath)

preprocess = Preprocess()

for filename in filenames:

    inferred_vector_list = []
    my_df = pd.DataFrame()

    for subdir, dirs, files in os.walk(os.path.join(rootpath, filename)):
        test_path, test_name = os.path.split(subdir)

        for file in files:

            # generator for train/test-reading
            # test_corpus = read_corpus(os.path.join(subdir, file), tokens_only=True)

            test_corpus = list(read_corpus(os.path.join(subdir, file), tokens_only=True))
            corpus = [item for sublist in test_corpus for item in sublist]  # to make a list out of list of lists
            # print(corpus)
            whole_document = " ".join(corpus)
            # print(whole_document)
            tokens = preprocess.clean(whole_document)
            # print (tokens)
            inferred_vector = model.infer_vector(tokens, alpha=0.0001, min_alpha=0.000001, epochs=300)
            a = inferred_vector.tolist()
            a.append(test_name)
            inferred_vector_list.append(a)

    my_df = my_df.append(inferred_vector_list)
    my_df.to_csv(filename + ".csv", index=False, header=False)
    data = pd.read_csv(filename + ".csv")
    print(filename + ".csv")
    print(data)
