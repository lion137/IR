# Functions to operate on index, and logic to parse a boolean query

from imports import *

def union(p1, p2):
    return set(p1).union(set(p2))

def intersect(p1, p2):
    return set(p1).intersection(set(p2))

def not_(p, ind):
    return set(ind).difference(set(p))

