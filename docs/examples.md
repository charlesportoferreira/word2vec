This this moment this tool can convert raw document into vectors
using the following embedding model:

* google word2vec
* fasttext
* glove
* elmo
* use
* mssa
* flexible lexical chain
* fixed lexical chain


Some of them has a particular method to call, so we are proving
examples of how to run each embedding model

### example of how to run:

google vectors

    python 3 wordvector/main.py -i datasets/toydata -o google.vec -m models/google.bin -t google 
