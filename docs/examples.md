Currently, this tool can convert raw document into vectors
using the following embedding model:

* google word2vec[link to the model]
* fasttext [link to the model]
* glove[link to the model]
* elmo[link to the model]
* use[link to the model]
* mssa[link to the model]
* flexible lexical chain[link to the model]
* fixed lexical chain[link to the model]


Some of them needs to be called with specific parameters, so we are proving
examples of how to run each embedding model and we will explain these flag
along the examples.


There are three mandatory input parameters:

-i -> a relative path to the corpus folder\
-o -> the name of the file that will be generated\
-m -> a relative path to the embedding model

### Example of how to run:

google model

    python 3 wordvector/main.py -i datasets/toydata -o google.vec -m models/google_model.bin -t google 
    
   