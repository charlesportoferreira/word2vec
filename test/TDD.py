import os
import sys
import unittest

import numpy

from wordvector.FileOperations import FileUtil
from wordvector.PreprocessUtil import Preprocess


class TestFileOperations(unittest.TestCase):

    def test_read_file(self):
        fu = FileUtil()
        self.assertEqual("the book is on the table\n", fu.read("file.txt"))

    def test_tokenizer(self):
        text = FileUtil().read("file.txt")
        tokens = Preprocess().clean(text)
        text2 = ""
        for token in tokens:
            text2 += " " + token
        self.assertEqual(" the book is on the table", text2)

    def test_average_numpy(self):
        array1 = numpy.full(4, 2)
        array2 = numpy.full(4, 3)
        matriz = numpy.array([array1, array2])
        array_mean = numpy.mean(matriz, axis=0)
        array_expected = [2.5, 2.5, 2.5, 2.5]
        self.compare_array(array_expected, array_mean)

    def compare_array(self, array_expected, array_mean):
        self.assertEqual(array_expected[0], array_mean[0])
        self.assertEqual(array_expected[1], array_mean[1])
        self.assertEqual(array_expected[2], array_mean[2])
        self.assertEqual(array_expected[3], array_mean[3])

    def test_add_array_dinamically(self):
        array1 = numpy.full(4, 2)
        array2 = numpy.full(4, 3)
        array3 = numpy.full(4, 7)
        l = []  # empty list
        l.append(array1)
        l.append(array2)
        l.append(array3)
        array_mean = numpy.mean(l, axis=0)
        array_expected = [4, 4, 4, 4]
        self.compare_array(array_expected, array_mean)

    def test_list_folder_names(self):
        fu = FileUtil()
        folder_root = "data2"
        folder_names = fu.get_folders(folder_root)
        names = ""
        for folder in folder_names:
            names += " " + folder

        self.assertEqual(" data2/a data2/c data2/d data2/b", names)

    def test_count_number_files_folder(self):
        sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
        file_util = FileUtil()
        number_files = file_util.count_files('data2/a')
        self.assertEqual(3, number_files)


if __name__ == '__main__':
    unittest.main()
