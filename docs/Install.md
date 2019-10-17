## How to install

### Requirements
You will need python 3.6 or later on your machine to run this code.
To check your python version type on a terminal:

       python3 --version
          
          
You should have an output similar to this:

        Python 3.6.8
        
To install python libraries onw may need a python installing package.
 We suggest to use [pip](https://pypi.org/project/pip/).

Download this repository to your local machine or clone it with git clone.

## Project folder structure:

After download it go to the respect folder. You should have a project folder with the following structure:

        word2vec
        |
        |-----main.py
        |-----Readme.md
        |-----datasets
        |-----models
        |-----test
        |-----wordvector
        
       
### Dataset folder
It is necessary to keep your corpus inside the dataset folder.
They need to be organized in a tree format. There is already a toydata example
 inside this folder. 
 
    toydata
       |---book
       |     |----> d1.txt
       |     |----> d2.txt
       |     |----> d3.txt
       |
       |---paper
             |----> d4.txt
             |----> d5.txt
             |----> d6.txt
            
            
This corpus is composed of 6 texts documents.
 Each document belongs to one of two classes: book or paper

After running the code one will end up with a file composed of 
6 vectors. One vector to each document. The numerical values will be separated by
commas and the last value is the label of the document

### Models folder
In this folder you need to keep your embeddings models

It is necessary to keep your corpus and models in the correct folder because 
we are using a relative path to find theses files. So 
if you put them in a parent folder from this project
it may not be able to find these files.


### Libraries:

You will need the following python libraries to run this code:
nltk, stop-words, gensim, tensorflow, tensorflow-hub.

One may install these libraries using the [pip](https://pypi.org/project/pip/) tool.
 To do that, run the following commands:

        pip install nltk
        pip install stop-words
        pip install gensim
        pip install tensorflow
        pip install tensorflow-hub


### Creating a python 3 virtual environment

It is not necessary to have a python virtual environment although
it is high recommend it to install it to avoid conflicts with other libraries

To create a virtual environment go to the project folder and type on a terminal:

    python3 -m venv env


To activate the virtual environment type:

    source env/bin/activate 

