# Word2Vector to arff
---
## Read text raw files, apply word2vec and generate a dataset in the arff format 
---
### To use type: 

**python3 wordvector/main.py [options]**

  Options:

        --input: 
          Relative path from your current folder to the to the folder with the 
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

        --output: 
          Name of the arff file that will be generated

        --model: 
          Relative path from your current folder to the word2vec trained model

        --type: 
          Select the type of model to use. Choices are: model, bin, txt 

        --aggregator: 
          [Optional parameter] Select between sum or mean. 
          Its set which way document vector will be generated
          Default = mean
        
        --noheader: 
          [Optinal parameter] Set True to save the vectors without header
          Default = False

        --preprocess:
          [Optional parameter] Set True to apply word tokenization. 
          Otherwise it will assume each row has one word.
          Default = False
