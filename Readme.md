# Convert text documents into numerical vectors
---
## Read the whole corpus and generate embedded vectors using word2vec/doc2vec pre-trained models
---

This tool reads a dataset composed of labeled text documents and generate numerical vectors using pre-trained models.
The primary goal of this tool is to provide a quick method to convert text documents into numerical matrix to 
use on machine learning tasks as document classification.

### How to Install

[installation guide](docs/Install.md)

To run this code you will need python 3.
We recommend to install a python virtual environment to run this code.

### To use type: 

[usage examples](docs/examples.md)

[TL_DR]\
**python3 wordvector/main.py [options]**

  Options:

        --help, -h:
          help instructions

        --input, -i: 
          Relative path from your current folder to the folder with the 
          raw txt files.

          The dataset must follow this tree structure:

          dataset_folder:
              |
              |---> folder_class1
              |      |---> file1.txt
              |      |---> file2.txt
              |      |---> filen.txt
              |
              |---> folder_class2
                     |---> file1.txt
                     |---> file2.txt
                     |---> filen.txt

        --output, -o: 
          Name of the arff file that will be generated

        --model, -m: 
          Relative path from your current folder to the word2vec trained model

        --type, -t: 
          Select the type of model to use. Choices are: mssa, glove, google, fasttext, elmo, use, doc2vec

        --aggregator, -a: 
          [Optional parameter] Select between sum or mean. 
          Its set which way document vector will be generated
          Default = mean
        
        --noheader, -n: 
          [Optional parameter] Set True to save the vectors without header
          Default = False

        --preprocess, -p:
          [Optional parameter] Set True to apply word tokenization. 
          Otherwise it will assume each row has one word.
          Default = False
          
        --doc, -d
          [Optional parameter] Set True to feed the model with
          all words as a single string

        
