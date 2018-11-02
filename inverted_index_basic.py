# information retrieval project, tests on text sample, building inverted index,
# preprocessed text, using nltk

"""2018 Copyleft lion137"""


from nltk.tokenize import word_tokenize, RegexpTokenizer


def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    tokens = [t.lower() for t in tokens]
    return tokens


def remove_duplicates(xs):
    s = []
    for x in xs:
        if x not in s:
            s.append(x)
    return s


def inv_index(xs):
    ls = []
    d = []
    t_el = xs[0][0]
    ls.append(xs[0][1])
    t_f = 1
    limit = len(xs)
    if limit == 1:
        d.append([[t_el, t_f], ls])
        return d
    for i in range(1, limit):
        if t_el == xs[i][0]:
            ls.append(xs[i][1])
            t_f += 1
            if i == limit - 1:
                d.append([[t_el, t_f], ls])
                return d
            continue
        d.append([[t_el, t_f], ls])
        ls =[]
        t_f = 0
        t_el = xs[i][0]
        t_f = 1
        ls.append(xs[i][1])
        if i == limit - 1:
            d.append([[t_el, t_f], ls])
    return d


def term_doc_id_list(xs):
    ys = []
    i = 1
    for ind, doc in enumerate(xs):
        ys += list(map(lambda x: [x, i], doc))
        i += 1
    return ys


def make_inverted_index(xs):
    """Makes inverted index from list of
    documents, working with RAM"""
    docs = map(tokenize, xs)
    docs = term_doc_id_list(docs)
    docs = sorted(docs)
    docs = remove_duplicates(docs)
    return inv_index(docs)


if __name__ == '__main__':
    doc = """I did enact Julius Caesar: I was killed
i’ the Capitol; Brutus killed me"""
    doc1 = """So let it be with Caesar.  The noble Brutus
hath told you Caesar was ambitious"""
    docs = [doc, doc1]

    print(make_inverted_index(docs))








