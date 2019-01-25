# Word2Vector to arff
---
## Read text raw files, apply word2vec and generate a dataset in the arff format 
---
### To use type: 

**python3 wordvector/main.py [options]**

  Options:

        --input: 
          Path to the folder with the raw txt files

        --output: 
          Name of the arff file that will be generated

        --model: 
          Path to the word2vec trained model

        --aggregator: 
          Select between sum or mean. Its set which way document vector will be generated

        --type: 
          Optional parameter. Select the type of model to use. Choices are: mssa, google, glove 

        --noheader: 
          Optinal parameter. Set true to just save the vectors 
