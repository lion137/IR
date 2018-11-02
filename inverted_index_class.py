# class with all the data

from imports import *
from texts import *


class InvertedIndex:
    def __init__(self, _data):
        self.data = [self.tokenize(e) for e in _data]
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

    def tokenize(self, text):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        tokens = [t.lower() for t in tokens]
        return tokens

    def get_postings(self, word):
        return self.index[word]

    def get_frequencies(self, word):
        return self.postings[word] if word in self.postings.keys() else "get_frequencies: word not in a list"


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            t = BinaryTree(newNode)
            self.leftChild = t
            t.parent = self
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.leftChild = self.leftChild
            self.leftChild.parent = t
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            t = BinaryTree(newNode)
            self.rightChild = t
            t.parent = self
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.rightChild = self.rightChild
            self.rightChild.parent = t
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getParent(self):
        return self.parent

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def setLeftChild(self, nodeObj):
        self.leftChild = nodeObj

    def setRightChild(self, nodeObj):
        self.rightChild = nodeObj

    def setParent(self, nodeObj):
        self.parent = nodeObj

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRoot(self):
        return


# boolean queries

def union(p1, p2):
    return set(p1).union(set(p2))


def intersect(p1, p2):
    return set(p1).intersection(set(p2))


def not_(p):
    return set(ind).difference(set(p))


def d_dict(docs):
    """Takes list of docs and their addresses and
    returns the same list of documents and a dict with
    strings 0, 1, 2 as keys and addresses """
    limit = len(docs)
    d = {}
    address_dict = {}
    for i in range(limit):
        d[str(i)], address_dict[str(i)] = docs[i][0], docs[i][1]
    return list(d.values()), address_dict

addresses_dict = d_dict(docs_tests)[1] ##
# parsing input and evaluation functions
def parse_word(w):
    return texts.get_postings(w)


def parse_input(exp):
    exp = exp.strip()
    if exp.isalpha(): exp = "~~" + exp
    exp_list = exp.replace('(', ' ( ').replace(')', ' ) ').replace('~', ' ~ ').split()
    for ind, e in enumerate(exp_list):
        if e == 'AND': exp_list[ind] = '&&'
        if e == 'OR':  exp_list[ind] = '||'
        if e == 'NOT': exp_list[ind] = '~'
    return exp_list


def eval_input(exp):
    s = evaluate_parse_tree(build_parse_tree(parse_input(exp)))
    return [addresses_dict[str(x)] for x in s]


# query parser


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorder_traversal(tree.getRightChild())


implication = lambda x, y: op.or_(op.not_(x), y)
equality = lambda x, y: op.and_(implication(x, y), implication(y, x))
xor = lambda x, y: op.and_(op.or_(x, y), op.not_(op.and_(x, y)))


def build_parse_tree(exp_list):
    e_tree = BinaryTree('')
    current_tree = e_tree
    for token in exp_list:
        if token == '(':
            current_tree.insertLeft('')
            current_tree = current_tree.getLeftChild()
        elif token in ['||', '&&', '->', '==', 'XR']:
            if current_tree.getRootVal() == '~':
                current_tree.getParent().setRootVal(token)
                current_tree.insertRight('')
                current_tree = current_tree.getRightChild()
            else:
                current_tree.setRootVal(token)
                current_tree.insertRight('')
                current_tree = current_tree.getRightChild()
        elif token == '~':
            current_tree.setRootVal('~')
            current_tree.insertLeft('')
            current_tree = current_tree.getLeftChild()
        elif token == ')':
            current_tree = current_tree.getParent()
        elif token not in ['(', ')', '||', '&&', '->', '~', 'XR', '==']:
            current_tree.setRootVal(parse_word(token))  # was int(token)
            current_tree = current_tree.getParent()
            if current_tree.getRootVal() == '~':
                current_tree = current_tree.getParent()
        else:
            raise ValueError
    return e_tree


def evaluate_parse_tree(tree):
    opers = {'||': union, '&&': intersect, '~': not_, '->': implication, '==': equality, 'XR': xor}
    leftT = tree.getLeftChild()
    rightT = tree.getRightChild()
    if leftT and not rightT:
        fn = opers[tree.getRootVal()]
        return fn(evaluate_parse_tree(leftT))
    elif leftT and rightT:
        fn = opers[tree.getRootVal()]
        return fn(evaluate_parse_tree(leftT), evaluate_parse_tree(rightT))
    else:
        return tree.getRootVal()


texts = InvertedIndex(d_dict(docs_tests)[0])
ind = texts.data_index
p1 = texts.get_postings("the")
p2 = texts.get_postings("european")
p3 = texts.get_postings('blabla')
p4 = texts.get_postings('brexit')
p5 = texts.get_postings('footballers')
postings_field = texts.postings
all_postings = texts.data_index
index_field = texts.index

form = "(the AND NOT(brexit OR NOT footballers))"
