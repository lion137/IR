# class with all the data

from imports import *


def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    tokens = [t.lower() for t in tokens]
    return tokens

class InvertedIndex:

    def __init__(self, _data):
        self.data = [tokenize(e) for e in _data]
        self.index, self.data_index = self.create_index(self.data)
        self.postings = self.make_dictionary(self.index)

    def create_index(self, data):
            index = defaultdict(list)
            data_index = []
            for i, tokens in enumerate(data):
                data_index.append(i)
                for token in tokens:
                    if i not in index[token]:
                        index[token].append(i)
            return index, data_index

    def make_dictionary(self, data):
        """returns a dictionary as a list of pairs:
        token and it's frequency"""
        tmp = (len(x) for x in data.values())
        d = {x: y for (x, y) in zip(data.keys(), tmp)}
        return d

    def get_postings(self, word):
        return self.index[word]

    def get_frequencies(self, word):
        return self.postings[word] if word in self.postings.keys() else "get_frequencies: word not in a list"





