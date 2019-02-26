import argparse


class CLWord2Vec:
    input_folder = None
    output_arff = None
    model_folder = None
    aggregator = "mean"
    isBin = False
    noHeader = False
    preprocess = False

    def __init__(self):
        parser = self.define_parser_parameters()
        args = parser.parse_args()

        self.input_folder = args.inf
        self.output_arff = args.ouf
        self.aggregator = args.agg
        self.model_folder = args.mod
        self.type = args.type
        self.noHeader = args.nohe
        self.preprocess = args.pre

    def define_parser_parameters(self):
        parser = argparse.ArgumentParser(description="Convert plain text documents into word embeddings")

        parser.add_argument('--aggregator', '-a', type=str, action='store', dest='agg',
                            required=False, choices=["sum", "mean"], default="mean",
                            help='type of aggregator to use  (default: %(default)s)')

        parser.add_argument('--noheader', '-n', type=bool, action='store', dest='nohe',
                            required=False, default=False, choices=[True, False],
                            help='set True to remove the arff header  (default: %(default)s)')

        parser.add_argument('--preprocess', '-p', type=bool, action='store', dest='pre',
                            required=False, choices=[True, False],
                            help='set True to apply word tokenization otherwise it will assume each row has one word '
                                 ' (default: %(default)s)',
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
                                   choices=["mssa", "google", "glove", "fasttext", "elmo"],
                                   help='select the type of model to load')

        return parser
