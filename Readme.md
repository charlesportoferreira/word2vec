# Word2Vector to arff

## Read text raw files, apply word2vec and generate a dataset in the arff format 


### To use type: 

**python3 wordvector/main.py --input folderName --output fileName.aff --model modelFolder --aggregator sum [--binary True] [--noheader True]**

        *--input*: Path to the folder with the raw txt files

        *--output*: Name of the arff file that will be generated

        *--model*: Path to the word2vec trained model

        *--aggregator*: Select between sum or mean. Its set which way document vector will be generated

        *--binary*: Optional parameter. Set true if you are using a binary model 
        *--noheader*: Optinal parameter. Set true to just save the vectors 
