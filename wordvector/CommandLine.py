import argparse


class CLWord2Vec:

    def __init__(self):
        parser = self.define_parser_parameters()
        args = parser.parse_args()

        self.input_folder = args.inf
        self.output_file = args.out
        self.aggregator = args.agg
        self.model_file = args.mod
        self.type = args.type
        self.is_arff_header = self.str2bool(args.arff_header)
        self.preprocess = self.str2bool(args.pre)
        self.doc2vec = self.str2bool(args.doc)
        self.is_full_path = self.str2bool(args.full_path)

    def define_parser_parameters(self):
        parser = argparse.ArgumentParser(description="Convert raw text documents into word embeddings")

        parser.add_argument('--aggregator', '-a', type=str, action='store', dest='agg',
                            required=False, choices=["sum", "mean"], default="mean",
                            help='type of aggregator to use  (default: %(default)s)')

        parser.add_argument('--arff-header', '-ah', type=str, action='store', dest='arff_header',
                            required=False, default="False", choices=['True', 'False'],
                            help='set True to add an arff header  (default: %(default)s)')

        parser.add_argument('--preprocess', '-p', type=str, action='store', dest='pre',
                            required=False, choices=['True', 'False'],
                            help='set True to apply word tokenization, stopword removal and lowercase. '
                                 'Otherwise it will assume each row has one word (default: %(default)s)',
                            default='True')

        parser.add_argument('--doc', '-d', type=str, action='store', dest='doc',
                            required=False, choices=['True', 'False'],
                            help='set True to feed the model with a single string containing all words. '
                                 '(default: %(default)s)',
                            default="False")

        parser.add_argument('--full', '-f', type=str, action='store', dest='full_path',
                            required=False, choices=['True', 'False'],
                            help='set True allow user to provide full path to input folder and model file. '
                                 '(default: %(default)s)',
                            default="False")

        required_args = parser.add_argument_group('required arguments')

        required_args.add_argument('--input', '-i', type=str, action='store', dest='inf', required=True,
                                   metavar="<path>",
                                   help='relative path from your current folder to the destination document folders')

        required_args.add_argument('--output', '-o', type=str, action='store', dest='out', metavar="<file_name>",
                                   required=True,
                                   help='name of the output file')

        required_args.add_argument('--model', '-m', type=str, action='store', dest='mod', required=True,
                                   metavar="<path>",
                                   help='relative path from your current folder to the trained word embedding model')

        required_args.add_argument('--type', '-t', type=str, action='store', dest='type', required=True,
                                   choices=["mssa", "google", "glove", "fasttext", "elmo", "use", "doc2vec"],
                                   help='select the type of model to load')

        return parser

    def str2bool(self, str_value):
        return str_value == "True"
