import errno
import glob
import os


class FileUtil:

    def read(self, file_name):
        text = ""
        try:
            f = open(file_name, errors="ignore")
            text = f.read()
            f.close()
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise ("problem reading file: " + file_name)
        return text

    def read_txt_folder(self, folder_name):
        files = self.get_files_path(folder_name)
        text = ""
        for fi in files:
            try:
                with open(fi) as f:
                    text += f.read()
                f.close()
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise ("problem reading file: " + fi)
        return text

    def get_files_path(self, folder_name):
        current = folder_name + "/*.txt"
        files = glob.glob(current)
        return files

    def get_current_path(self):
        return os.path.dirname(os.path.realpath(__file__))

    def get_folders(self, folder_root):
        folders = []
        for dirname, dirnames, filenames in os.walk(folder_root):
            for subdirname in dirnames:
                folders.append(os.path.join(dirname, subdirname))

        return folders

    def remove_last_character(self, data):
        return data[:-1]

    def get_labels(self, folders_path):
        labels = []
        for folder in folders_path:
            labels.append(self.get_label(folder))
        return labels

    def get_label(self, folder_path):
        data = folder_path.split("/")
        return data[len(data) - 1]


class ArffUtil:
    def get_header(self, num_features, labels):
        title = "@RELATION w2v"
        features = self.create_features(labels, num_features)
        return title + "\n\n" + features + "\n"

    def create_features(self, labels, num_features):
        features = ""
        for i in range(num_features):
            features += "@ATTRIBUTE f" + str(i) + " REAL\n"
        features += "@ATTRIBUTE class {"
        for label in labels:
            features += str(label + ",")
        features = FileUtil().remove_last_character(features)
        features += "}\n\n@DATA"
        return features

    def get_instance(self, doc_vector):
        data = ""
        for feature in doc_vector:
            data += feature + ","
        data = FileUtil().remove_last_character(data)
        data += "\n"
        return data
