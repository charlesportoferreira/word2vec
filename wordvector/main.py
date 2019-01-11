import errno
import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)
# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from wordvector.CommandLine import CLWord2Vec
from wordvector.FileOperations import FileUtil, ArffUtil
from wordvector.PreprocessUtil import Preprocess
from wordvector.Word2vec import Word2VectorUtil

commandLine = CLWord2Vec()

in_foname = os.path.join(ppydir_name, commandLine.input_folder)
mo_foname = os.path.join(ppydir_name, commandLine.model_folder)

# ################################# simulation #########################################################################
# w2v = Word2VectorUtil(aggregator=commandLine.aggregator, model_path=mo_foname, simulation=True)
# ######################################################################################################################

w2v = Word2VectorUtil(aggregator=commandLine.aggregator, model_path=mo_foname, binary=commandLine.isBin)
preprocess = Preprocess()
file_util = FileUtil()
arff_util = ArffUtil()

text = ""
folders = file_util.get_folders(in_foname)
labels = file_util.get_labels(folders)
number_features = w2v.number_features
header = arff_util.get_header(number_features, labels)

f = open(commandLine.output_arff, 'w', errors="ignore")
f.write(header)

for folder in folders:  # reading class folders
    print("processing folder: " + folder)
    files_path = file_util.get_files_path(folder)
    for fi in files_path:
        text = file_util.read(fi)
        if commandLine.isBin:
            tokens = preprocess.clean(text)
        else:
            tokens = text.split("\n")
        if len(tokens) == 0:
            continue  # empty document
        label = file_util.get_label(folder)
        doc_vector = w2v.get_doc_vector(tokens, label)  # create a document vector
        if len(doc_vector) == 0:
            continue  # no vector found to this document
        instance = arff_util.get_instance(doc_vector)
        f.write(instance)
f.close()
quit()
