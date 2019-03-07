import nltk as nltk
from stop_words import get_stop_words

nltk.download('punkt', quiet=True)


class Preprocess:
    stopWords = get_stop_words('en')  # list of stopwords/english PyPl

    def clean(self, text):
        tokens = self.tokenize(text)
        words_lowercase = self.lowercase(tokens)
        words_after_stopremoval = self.removeStopWords(words_lowercase)
        return words_after_stopremoval

    def lowercase(self, tokens):
        return [w.lower() for w in tokens]

    def tokenize(self, text):
        return nltk.word_tokenize(text)

    def removeStopWords(self, words):
        words = [w for w in words if w not in self.stopWords]
        return words
