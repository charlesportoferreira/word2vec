# Convert text documents into numerical vectors
---
## Read the whole corpus and generate embedded vectors using word2vec/doc2vec pre-trained models
---

This tool reads a dataset composed of labeled text documents and generates numerical vectors using pre-trained models.
The primary goal of this tool is to provide a quick method to convert text documents into a numerical matrix to 
use on machine learning tasks as document classification.

### How to Install

[installation guide](docs/Install.md)


### How to use 

[usage examples](docs/examples.md)


---
### Overview

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
        
        --arff-header, -ah: 
          [Optional parameter] Set True to add an arff compatible header to the output file
          Default = False

        --preprocess, -p:
          [Optional parameter] Set False to avoid preprocessing, however it will assume each row has one word.
          If it is True, will apply word tokenization, stopword removal and word lowercase.
          Default = True 
          
        --doc, -d
          [Optional parameter] Set True to feed the model with
          all words as a single string
          
        --full-path, -f
          [Optional parameter] Set True to allow full path on input data and model file, instead
          of relative path.
          Default = False

        
### Changelog 

[Changelog](docs/changelog.md)
