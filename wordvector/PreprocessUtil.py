import nltk as nltk

nltk.download('punkt', quiet=True)


class Preprocess:

    def clean(self, text):
        tokens = self.tokenize(text)
        words_lowercase = self.lowercase(tokens)
        return words_lowercase

    def lowercase(self, tokens):
        return [w.lower() for w in tokens]

    def tokenize(self, text):
        return nltk.word_tokenize(text)
