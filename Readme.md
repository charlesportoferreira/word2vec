# Word2Vector to arff
---
## Read text raw files, apply word2vec and generate a dataset in the arff format 
---
### To use type: 

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
          Select the type of model to use. Choices are: mssa, glove, google, fasttext, elmo, use 

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

        
