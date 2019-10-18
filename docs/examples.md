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

##### google embedding

    python3 wordvector/main.py -i datasets/toydata -o google.vec -m models/google_model.bin -t google 
    
##### glove embedding

    python3 wordvector/main.py -i datasets/toydata -o glove.vec -m models/glove_model.txt -t glove 

##### fasttext embedding

    python3 wordvector/main.py -i datasets/toydata -o fasttext.vec -m models/fasttext_model.txt -t fasttext 

##### mssa embedding

Mssa embedding model need a corpus properly parsed as 
suggest by the original paper. We are also providing the same toydata
with this format as example

    python3 wordvector/main.py -i dataset/toydata_parsed/ -o toydata_mssa.vec  -m models/mssa.model -t mssa  -p False
    
    
One may notice we provided the parameter -p False. This is because our toydata_parsed
is already preprocessed and each token is in one line of the document. Thus is the format
that mssa model is expecting. 
    
 
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
