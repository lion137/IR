# tests

from imports import *
from texts import *
from inverted_index_class import *
from inverted_index_functions import *
import main as mn

## Test base query functions

def test_not_for_postings_list():
    assert ( not_(mn.p3) ==  {0, 1, 2, 3})

def test_union_for_posting_lists():
    assert union(mn.p1, mn.p2) == {0, 1, 2, 3}

def test_intersect_for_posting_lists():
    assert intersect(mn.p1, mn.p2) == {0}

def test_not_with_union():
    assert union(mn.p1, not_(mn.p2)) == {0, 2, 3}

def test_not_union_and_intersect():
    assert intersect(mn.p1, not_(union(mn.p4, not_(mn.p5)))) == {0}

## Test InvertedIndex class fields

def test_keys_of_postings_field():
    assert mn.postings_field.keys().__repr__() == """dict_keys(['footballers', 'from', 'countries', 'in', 'the', 'european', 'union', 'and', 'economic', 'area', 'to', 'get', 'a', 'work', 'permit', 'player', 'has', 'governing', 'body', 'endorsement', 'after', 'brexit', 'regulations', 'that', 'currently', 'apply', 'those', 'outside', 'we', 're', 'all', 'keen', 'something', 'works', 'pretty', 'much', 'as', 'way', 'it', 'does', 'now', 'but', 'can', 't'])"""

def test_values_of_postings_field():
    assert mn.postings_field.values().__repr__() ==  """dict_values([1, 1, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])"""

def test_all_postings_field():
    assert mn.texts.data_index == [0, 1, 2, 3]

def test_index_field():
    assert mn.texts.index.__repr__() == """defaultdict(<class 'list'>, {'footballers': [0], 'from': [0], 'countries': [0], 'in': [0], 'the': [0, 2, 3], 'european': [0, 1], 'union': [0, 2], 'and': [0], 'economic': [0, 2], 'area': [0, 2], 'to': [1, 2, 3], 'get': [1, 3], 'a': [1], 'work': [1], 'permit': [1], 'player': [1], 'has': [1], 'governing': [1], 'body': [1], 'endorsement': [1], 'after': [2], 'brexit': [2], 'regulations': [2], 'that': [2, 3], 'currently': [2], 'apply': [2], 'those': [2], 'outside': [2], 'we': [3], 're': [3], 'all': [3], 'keen': [3], 'something': [3], 'works': [3], 'pretty': [3], 'much': [3], 'as': [3], 'way': [3], 'it': [3], 'does': [3], 'now': [3], 'but': [3], 'can': [3], 't': [3], 'blabla': []})"""

def test_data_field():
    assert mn.texts.data.__repr__() == """[['footballers', 'from', 'countries', 'in', 'the', 'european', 'union', 'and', 'european', 'economic', 'area'], ['to', 'get', 'a', 'work', 'permit', 'a', 'player', 'has', 'to', 'get', 'a', 'governing', 'body', 'endorsement', 'european'], ['after', 'brexit', 'the', 'regulations', 'that', 'currently', 'apply', 'to', 'those', 'outside', 'the', 'economic', 'union', 'area'], ['we', 're', 'all', 'keen', 'to', 'get', 'something', 'that', 'works', 'pretty', 'much', 'as', 'the', 'way', 'it', 'does', 'now', 'but', 'we', 'can', 't']]"""

def test_get_frequencies():
    w = "the"
    assert mn.texts.get_frequencies(w) == 3

def test_get_postings():
    w = "the"
    assert mn.texts.get_postings(w) == [0, 2, 3]

##


