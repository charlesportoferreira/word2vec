Currently, this tool can convert raw documents into vectors
using the following embedding model:

* google word2vec [link to the model][link to the paper]
* fastText [link to the model][link to the paper]
* Glove [link to the model][link to the paper]
* Elmo [link to the model][link to the paper]
* USE [link to the model][link to the paper]
* Mssa [link to the model][link to the paper]


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

    python3 wordvector/main.py -i datasets/toydata -o google.vec -m models/google_model.bin -t google 
    
##### Glove embedding

    python3 wordvector/main.py -i datasets/toydata -o glove.vec -m models/glove_model.txt -t glove 

##### fastText embedding

    python3 wordvector/main.py -i datasets/toydata -o fasttext.vec -m models/fasttext_model.txt -t fasttext 

##### MSSS embedding

Mssa embedding model need a corpus properly parsed and preprocessed as 
suggest by the original paper. We are also providing a toydata_parsed
with this format as example. 


 Since this dataset is already parsed and preprocessed
we need to provide an additional parameter to inform that it is not necessary to
apply any preprocessing:
 
    -p --> set False to disable preprocessing 
    
To run mssa embedding, type:

    python3 wordvector/main.py -i dataset/toydata_parsed/ -o toydata_mssa.vec  -m models/mssa.model -t mssa  -p False
    
    

##### Elmo embedding

To run Elmo it is not necessary to provide a embedding model 
because our tool will fetch it from the web. So, one may set
any value to the parameter -m. 

    python3 wordvector/main.py -i datasets/toydata -o elmo.vec -m nothing -t elmo 
    
    

##### USE embedding

The same happens with USE, i.e, it is not necessary to provide
a model.

    python3 wordvector/main.py -i datasets/toydata -o use.vec -m nothing -t use 
    
 
### Generating a Weka compatible file

One may want to run experiments with [Weka](https://www.cs.waikato.ac.nz/ml/weka/).
In this case, it is necessary to set a flag that allows converting the output file into a Weka
compatible format
 
 There is one parameter to add :
 
    -ah --> set True to enable arff compatibility 

##### example with google embedding
    
    
     python3 wordvector/main.py -i datasets/toydata -o google.arff -m models/google_model.bin -t google -ah True   
     
 Basically, the output file will have a header and attribute description compatible with
 the arff format.
