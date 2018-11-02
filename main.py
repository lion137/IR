
from imports import *
from texts import *
from inverted_index_class import *


def docs_dict(docs):
    """Takes list of docs and their addresses and
    returns the same list of documents and a dict with
    strings 0, 1, 2 as keys and addresses """
    limit = len(docs)
    d = {}
    address_dict = {}
    for i in range(limit):
        d[str(i)], address_dict[str(i)] = docs[i][0], docs[i][1]
    return list(d.values()), address_dict

texts = InvertedIndex(d_dict(docs_tests)[0])
p1 = texts.get_postings("the")
p2 = texts.get_postings("european")
p3 = texts.get_postings('blabla')
p4 = texts.get_postings('brexit')
p5 = texts.get_postings('footballers')
postings_field = texts.postings
all_postings = texts.data_index
index_field = texts.index

form = "(the AND NOT(brexit OR NOT footballers))"

if __name__ == '__main__':
    print(parse_input(form))
    print(eval_input(form))
    #print(d_dict(docs_tests))


