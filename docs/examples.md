[\[back\]](../Readme.md)

Currently, this tool can convert raw documents into vectors
using the following embedding model:

* Google word2vec: 
[pre-trained model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)
([paper1](http://arxiv.org/pdf/1301.3781.pdf), [paper2](http://arxiv.org/pdf/1301.3781.pdf), [paper3](http://arxiv.org/pdf/1301.3781.pdf))
* fastText: [pre-trained model](https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M-subword.vec.zip)
([paper](https://arxiv.org/abs/1712.09405))
* Glove: [pre-trained model](http://nlp.stanford.edu/data/glove.6B.zip)
([paper](https://nlp.stanford.edu/pubs/glove.pdf))
* MSSA: [link to the model](https://deepblue.lib.umich.edu/data/downloads/1r66j1149?locale=en) 
([paper](https://www.sciencedirect.com/science/article/pii/S0957417419304269))
* ELMo: ([paper](https://arxiv.org/pdf/1802.05365))
* USE: ([paper](https://arxiv.org/pdf/1803.11175))


Some of them need to be called with specific parameters, so we are proving
examples of how to run each embedding model and we will explain these flag
along with the examples.


There are four mandatory input parameters:

    -i --> a relative path to the corpus folder
    -o --> the name of the file that will be generated
    -m --> a relative path to the embedding model
    -t --> type of word embedding model
    
It is necessary to inform the type of the embedding model because each model have 
a different strategy to access its vector. This strategy depends on the model file
file format and the support library used to handle the model

### Example of how to run:

##### Google embedding

    python3 wordvector/main.py -i dataset/toydata -o google.vec -m models/GoogleNews-vectors-negative300.bin -t google 
    
After executing you should have an output simliar to this one:


    loading embedding model...
    done!
    model-size:	 300
    
    processing folder: path_to_the_project/word2vec/dataset/toydata_parsed/book
    done 3 of 3 100%
    
    processing folder: path_to_the_project/word2vec/dataset/toydata_parsed/paper
    done 3 of 3 100%

##### Glove embedding

    python3 wordvector/main.py -i dataset/toydata -o glove.vec -m models/glove_model.txt -t glove 

##### fastText embedding

    python3 wordvector/main.py -i dataset/toydata -o fasttext.vec -m models/wiki-news-300d-1M-subword.vec -t fasttext 

##### MSSA embedding

Mssa embedding model needs a corpus properly parsed and preprocessed as 
suggested by the original paper. We are also providing a toydata_parsed
with this format as example. 


 Since this dataset is already parsed and preprocessed
we need to provide an additional parameter to inform that it is not necessary to
apply any preprocessing:
 
    -p --> set False to disable preprocessing 
    
To run mssa embedding, type:

    python3 wordvector/main.py -i dataset/toydata_parsed/ -o toydata_mssa.vec  -m models/mssa.model -t mssa  -p False
    
##### ELMo embedding

To run Elmo it is not necessary to provide a embedding model 
because our tool will fetch it from the web. So, one may set
any value to the parameter -m. 

    python3 wordvector/main.py -i dataset/toydata -o elmo.vec -m nothing -t elmo 
    
##### USE embedding

The same happens with USE, i.e, it is not necessary to provide
a model.

    python3 wordvector/main.py -i dataset/toydata -o use.vec -m nothing -t use 
    
### Generating a Weka compatible file

One may want to run experiments with [Weka](https://www.cs.waikato.ac.nz/ml/weka/).
In this case, it is necessary to set a flag that allows converting the output file into a Weka
compatible format
 
 There is one parameter to add :
 
    -ah --> set True to enable arff compatibility 

##### example with google embedding
    
     python3 wordvector/main.py -i dataset/toydata -o google.arff -m models/google_model.bin -t google -ah True   
     
 Basically, the output file will have a header and attribute description compatible with
 the arff format.
 
 
[\[back\]](../Readme.md)
