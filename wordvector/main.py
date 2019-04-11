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


class Main:
    # TODO: check if we are working with the wrong model
    # TODO: add an option to give a full path for input and model

    def main(self):
        command_line = CLWord2Vec()

        in_foname = os.path.join(ppydir_name, command_line.input_folder)
        mo_foname = os.path.join(ppydir_name, command_line.model_folder)

        # ################################# simulation #################################################################
        # w2v = Word2VectorUtil(aggregator=command_line.aggregator, model_path=mo_foname, simulation=True)
        # ##############################################################################################################

        preprocess = Preprocess()
        file_util = FileUtil()
        arff_util = ArffUtil()

        folders = file_util.get_folders(in_foname)  # reading class folders
        self.check_folders_exist(folders, in_foname)

        labels = file_util.get_labels(folders)  # extracting labels
        w2v = Word2VectorUtil(aggregator=command_line.aggregator, model_path=mo_foname, model_type=command_line.type)
        number_features = w2v.number_features
        relation_name = file_util.get_model_name(command_line.model_folder)
        header = arff_util.get_header(number_features, labels, relation_name)

        f = open(command_line.output_arff, 'w', errors="ignore")
        if not command_line.noHeader:
            f.write(header)

        empty_doc = 0
        doc_without_vector = 0
        for folder in folders:
            doc_vector_counter = 0
            label = file_util.get_label(folder)
            print("\nprocessing folder: " + folder)
            number_files = file_util.count_files(folder)
            count = 0
            files = file_util.get_files_path(folder)
            for file in files:
                text = file_util.read(file)
                if command_line.preprocess:
                    tokens = preprocess.clean(text)
                    if command_line.doc2vec:
                        list_single_string = [" ".join(tokens)]
                        tokens = list_single_string
                else:
                    tokens = text.split("\n")
                if len(tokens) == 0:
                    empty_doc += 1
                    continue  # empty document
                doc_vector = w2v.get_doc_vector(tokens)  # create a document vector
                if len(doc_vector) == 0:
                    doc_without_vector += 1
                    continue  # no vector found to this document
                doc_vector_counter += 1
                instance = arff_util.get_instance(doc_vector, label)
                f.write(instance)
                count += 1
                percentage = str(round(100 * count / number_files))
                print("done " + str(count) + " of " + str(number_files) + " " + percentage + "%\r", end='')

            self.check_folder_with_no_vectors(doc_vector_counter, label)
        print()
        print("empty docs: " + str(empty_doc))
        print("docs with no vectors: " + str(doc_without_vector))
        f.close()

    def check_folder_with_no_vectors(self, doc_vector_counter, label):
        if doc_vector_counter == 0:
            print("-----------------------------------------------------------------------------------------------")
            print("no vectors found with this folder: " + label)
            print("-----------------------------------------------------------------------------------------------")

    def check_folders_exist(self, folders, in_foname):
        if not folders:
            print("----------------------------------------------------------------------------------------------")
            print("not possible to find any folder at: " + in_foname)
            print("check if the path to the input folder is correct or the folder is empty")
            print("----------------------------------------------------------------------------------------------")
            quit()


if __name__ == "__main__":
    Main().main()
