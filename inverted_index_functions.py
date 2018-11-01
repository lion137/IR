# Functions to operate on index, and logic to parse a boolean query

from imports import *
import main as mn
import inverted_index_class as inv

# boolean queries

ind = mn.texts.data_index

def union(p1, p2):
    return set(p1).union(set(p2))

def intersect(p1, p2):
    return set(p1).intersection(set(p2))

def not_(p):
    return set(ind).difference(set(p))


# query parser

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


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorder_traversal(tree.getRightChild())


implication = lambda x, y: op.or_(op.not_(x), y)
equality = lambda x, y: op.and_(implication(x, y), implication(y, x))
xor = lambda x, y: op.and_(op.or_(x, y), op.not_(op.and_(x, y)))

# parsing input and evaluation functions
def parse_word(w):
    return mn.texts.get_postings(w)

def parse_input(exp):
    exp = exp.strip()
    if exp.isalpha(): exp = "~~" + exp
    exp_list = exp.replace('(', ' ( ').replace(')', ' ) ').replace('~', ' ~ ').split()
    for ind, e in enumerate(exp_list):
        if   e == 'AND': exp_list[ind] = '&&'
        if   e == 'OR':  exp_list[ind] = '||'
        if   e == 'NOT': exp_list[ind] = '~'
    return exp_list

def eval_input(exp):
    return evaluate_parse_tree(build_parse_tree(parse_input(exp)))

def build_parse_tree(exp_list):
    #exp_list = exp.replace('(', ' ( ').replace(')', ' ) ').replace('~', ' ~ ').split()
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
        else:
            current_tree.setRootVal(parse_word(token))  # was int(token)
            current_tree = current_tree.getParent()
            if current_tree.getRootVal() == '~':
                current_tree = current_tree.getParent()
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
