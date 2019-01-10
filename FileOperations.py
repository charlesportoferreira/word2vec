import errno
import glob
import os


class FileUtil:

    def read(self, fileName):
        f = open("file.txt")
        text = f.read()
        f.close()
        return text

    def read_txt_folder(self, folder_name):
        files = self.get_files_path(folder_name)
        text = ""
        for fi in files:
            try:
                with open(fi) as f:
                    text += f.read()
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise ("problem reading file: " + fi)
        return text

    def get_files_path(self, folder_name):
        # current = self.get_current_path()
        # current += "/" + folder_name + "/*.txt"
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

    def save_dataset_as_arff(self, dataset, file_name):
        self.save_header(dataset, file_name)
        self.save_data(dataset, file_name)

    def save_header(self, dataset, file_name):
        title = "@RELATION w2v"
        features = self.get_features(dataset)
        with open(file_name, 'w') as f:
            f.write(title + "\n\n" + features + "\n")
            f.close()

    def get_features(self, dataset):
        num_features = self.get_num_features(dataset)
        labels = self.get_labels(dataset)
        features = self.create_features(labels, num_features)
        return features

    def create_features(self, labels, num_features):
        features = ""
        for i in range(num_features - 1):
            features += "@ATTRIBUTE f" + str(i) + " REAL\n"
        features += "@ATTRIBUTE class {"
        for label in labels:
            features += str(label + ",")
        features = self.remove_last_character(features)
        features += "}\n\n@DATA"
        return features

    def get_labels(self, dataset):
        labels = set()
        for doc in dataset:
            labels.add(doc[-1])
        list_labels = list(labels)
        list_labels.sort()
        return list_labels

    def get_num_features(self, dataset):
        doc = dataset[0]
        num_features = len(doc)
        return num_features

    def save_data(self, dataset, file_name):
        count = 0
        with open(file_name, 'a+') as f:
            for doc in dataset:
                data = ""
                for feature in doc:
                    data += feature + ","
                data = self.remove_last_character(data)
                data += "\n"
                count = count + 1
                f.write(data)
                print("done: " + str(count) + " of " + str(len(dataset)) + "\r", end='')
            f.close()
        print()
        return

    def remove_last_character(self, data):
        return data[:-1]
