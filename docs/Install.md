## How to install

### requirements
You will need python 3.6 or later on your machine to run this code.
To check your python version type on a terminal:

       python3 --version
          
          
You should have an output similar to this:

        Python 3.6.8
        
You will also need a python installing package. We recommend to use 
[pip](https://pypi.org/project/pip/).

Download this repository to your machine or clone it.

## project folder structure:

After download it go to the respect folder. You should have a project folder with the following structure:

        word2vec
        |
        |-----main.py
        |-----Readme.md
        |-----datasets
        |-----models
        |-----test
        |-----wordvector
        
       
### Datasets folder
You will keep your corpus inside the datasets folder.
They need to be organized in a tree format. There is already a toydata example
 inside this folder. 

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


