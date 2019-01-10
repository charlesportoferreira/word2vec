import errno
import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)
# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from wordvector.CommandLine import CLWord2Vec
from wordvector.FileOperations import FileUtil
from wordvector.PreprocessUtil import Preprocess
from wordvector.Word2vec import Word2VectorUtil


def get_label(folder_path):
    data = folder_path.split("/")
    return data[len(data) - 1]


commandLine = CLWord2Vec()

in_foname = os.path.join(ppydir_name, commandLine.input_folder)
mo_foname = os.path.join(ppydir_name, commandLine.model_folder)

# w2v = Word2VectorUtil(aggregator=commandLine.aggregator, model_path=mo_foname, simulation=True,
#                       simulation_value=3)
w2v = Word2VectorUtil(aggregator=commandLine.aggregator, model_path=mo_foname, binary=commandLine.isBin)
preprocess = Preprocess()
fileUtil = FileUtil()

text = ""
folders = fileUtil.get_folders(in_foname)
list_doc_vec = []
for folder in folders:  # reading class folders
    print("processing folder: " + folder)
    files_path = fileUtil.get_files_path(folder)
    for fi in files_path:
        try:
            with open(fi, errors="ignore") as f:  # reading document files
                text = f.read()
                if commandLine.isBin:
                    tokens = preprocess.clean(text)
                else:
                    tokens = text.split("\n")
                if len(tokens) == 0:
                    continue  # empty document
                label = get_label(folder)
                doc_vector = w2v.get_doc_vector(tokens, label)  # create a document vector
                if len(doc_vector) == 0:
                    continue  # no vector found to this document
                list_doc_vec.append(doc_vector)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise ("problem reading file: " + fi)

if len(list_doc_vec) == 0:
    print("no documents")
    quit()

print("saving arff...")
fileUtil.save_dataset_as_arff(list_doc_vec, commandLine.output_arff)

quit()
