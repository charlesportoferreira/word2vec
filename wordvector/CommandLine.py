import argparse


class CLWord2Vec:
    input_folder = None
    output_arff = None
    model_folder = None
    aggregator = "mean"
    isBin = False
    noHeader = False
    preprocess = False
    doc2vec = False

    def __init__(self):
        parser = self.define_parser_parameters()
        args = parser.parse_args()

        self.input_folder = args.inf
        self.output_arff = args.ouf
        self.aggregator = args.agg
        self.model_folder = args.mod
        self.type = args.type
        self.noHeader = self.str2bool(args.nohe)
        self.preprocess = self.str2bool(args.pre)
        self.doc2vec = self.str2bool(args.doc)

    def define_parser_parameters(self):
        parser = argparse.ArgumentParser(description="Convert plain text documents into word embeddings")

        parser.add_argument('--aggregator', '-a', type=str, action='store', dest='agg',
                            required=False, choices=["sum", "mean"], default="mean",
                            help='type of aggregator to use  (default: %(default)s)')

        parser.add_argument('--noheader', '-n', type=str, action='store', dest='nohe',
                            required=False, default=False, choices=['True', 'False'],
                            help='set True to remove the arff header  (default: %(default)s)')

        parser.add_argument('--preprocess', '-p', type=str, action='store', dest='pre',
                            required=False, choices=['True', 'False'],
                            help='set True to apply word tokenization, stopword removal and lowercase. '
                                 'Otherwise it will assume each row has one word (default: %(default)s)',
                            default=False)

        parser.add_argument('--doc', '-d', type=str, action='store', dest='doc',
                            required=False, choices=['True', 'False'],
                            help='set True to feed the model with a single string containing all words. '
                                 '(default: %(default)s)',
                            default=False)

        required_args = parser.add_argument_group('required arguments')

        required_args.add_argument('--input', '-i', type=str, action='store', dest='inf', required=True,
                                   metavar="<path>",
                                   help='relative path from your current folder to the destination document folders')

        required_args.add_argument('--output', '-o', type=str, action='store', dest='ouf', metavar="<file_name>",
                                   required=True,
                                   help='name of the output file')

        required_args.add_argument('--model', '-m', type=str, action='store', dest='mod', required=True,
                                   metavar="<path>",
                                   help='relative path from your current folder to the trained word embedding model')

        required_args.add_argument('--type', '-t', type=str, action='store', dest='type', required=True,
                                   choices=["mssa", "google", "glove", "fasttext", "elmo", "use"],
                                   help='select the type of model to load')

        return parser

    def str2bool(self, str_value):
        return str_value == "True"
