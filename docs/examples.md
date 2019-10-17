Currently, this tool can convert raw documents into vectors
using the following embedding model:

* google word2vec [link to the model][link to the paper]
* fastText [link to the model][link to the paper]
* Glove [link to the model][link to the paper]
* Elmo [link to the model][link to the paper]
* USE [link to the model][link to the paper]
* Mssa [link to the model][link to the paper]
* flexible lexical chain [link to the model][link to the paper]
* fixed lexical chain [link to the model][link to the paper]


Some of them need to be called with specific parameters, so we are proving
examples of how to run each embedding model and we will explain these flag
along with the examples.


There are four mandatory input parameters:

    -i --> a relative path to the corpus folder
    -o --> the name of the file that will be generated
    -m --> a relative path to the embedding model
    -t --> type of word embedding model
    
    
It is necessary to inform the type of the embedding model because each model have 
a different strategy to access its data. This strategy depends on the model file
file format and the support library used to handle the model

### Example of how to run:

*google model


    python3 wordvector/main.py -i datasets/toydata -o google.vec -m models/google_model.bin -t google 
    
 
### Generating a Weka compatible file

One may want to run experiments with [Weka](https://www.cs.waikato.ac.nz/ml/weka/).
In this case, it is necessary to set a flag that allows converting the output file into a Weka
compatible format
 
 There is one parameter to add :
 
    -ar --> set True to enable arff compatibility 

*example with google embedding
    
    
     python3 wordvector/main.py -i datasets/toydata -o google.arff -m models/google_model.bin -t google -ah True   
     
 Basically, the output file will have a header and attribute description compatible with
 the arff format.
