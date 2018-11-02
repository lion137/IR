# tests

import pytest
from inverted_index_class import *


## Test base query functions

def test_not_for_postings_list():
    assert (not_(p3) == {0, 1, 2, 3})


def test_union_for_posting_lists():
    assert union(p1, p2) == {0, 1, 2, 3}


def test_intersect_for_posting_lists():
    assert intersect(p1, p2) == {0}


def test_not_with_union():
    assert union(p1, not_(p2)) == {0, 2, 3}


def test_not_union_and_intersect():
    assert intersect(p1, not_(union(p4, not_(p5)))) == {0}


## Test InvertedIndex class fields

def test_keys_of_postings_field():
    assert postings_field.keys().__repr__() == """dict_keys(['footballers', 'from', 'countries', 'in', 'the', 'european', 'union', 'and', 'economic', 'area', 'to', 'get', 'a', 'work', 'permit', 'player', 'has', 'governing', 'body', 'endorsement', 'after', 'brexit', 'regulations', 'that', 'currently', 'apply', 'those', 'outside', 'we', 're', 'all', 'keen', 'something', 'works', 'pretty', 'much', 'as', 'way', 'it', 'does', 'now', 'but', 'can', 't'])"""


def test_values_of_postings_field():
    assert postings_field.values().__repr__() == """dict_values([1, 1, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])"""


def test_all_postings_field():
    assert texts.data_index == [0, 1, 2, 3]


def test_index_field():
    assert texts.index.__repr__() == """defaultdict(<class 'list'>, {'footballers': [0], 'from': [0], 'countries': [0], 'in': [0], 'the': [0, 2, 3], 'european': [0, 1], 'union': [0, 2], 'and': [0], 'economic': [0, 2], 'area': [0, 2], 'to': [1, 2, 3], 'get': [1, 3], 'a': [1], 'work': [1], 'permit': [1], 'player': [1], 'has': [1], 'governing': [1], 'body': [1], 'endorsement': [1], 'after': [2], 'brexit': [2], 'regulations': [2], 'that': [2, 3], 'currently': [2], 'apply': [2], 'those': [2], 'outside': [2], 'we': [3], 're': [3], 'all': [3], 'keen': [3], 'something': [3], 'works': [3], 'pretty': [3], 'much': [3], 'as': [3], 'way': [3], 'it': [3], 'does': [3], 'now': [3], 'but': [3], 'can': [3], 't': [3], 'blabla': []})"""


def test_data_field():
    assert texts.data.__repr__() == """[['footballers', 'from', 'countries', 'in', 'the', 'european', 'union', 'and', 'european', 'economic', 'area'], ['to', 'get', 'a', 'work', 'permit', 'a', 'player', 'has', 'to', 'get', 'a', 'governing', 'body', 'endorsement', 'european'], ['after', 'brexit', 'the', 'regulations', 'that', 'currently', 'apply', 'to', 'those', 'outside', 'the', 'economic', 'union', 'area'], ['we', 're', 'all', 'keen', 'to', 'get', 'something', 'that', 'works', 'pretty', 'much', 'as', 'the', 'way', 'it', 'does', 'now', 'but', 'we', 'can', 't']]"""


def test_get_frequencies():
    w = "the"
    assert texts.get_frequencies(w) == 3


def test_get_postings():
    w = "the"
    assert texts.get_postings(w) == [0, 2, 3]


## Input formula evaluation tests

def test_eval_input():
    assert eval_input(form) == [r0]


def test_eval_input_single_word():
    assert eval_input("the") == [r0, r2, r3]


## Test user input

def test_enter_to_prompt_function():
    assert eval_input("(the AND NOT(brexit OR NOT footballers))") == [r0]
    with pytest.raises(AttributeError):
        eval_input("not the")


@pytest.mark.parametrize("arg, ret", [("(NOT countries AND NOT brexit)", [r1, r3]),
                                      ("NOT NOT the", [r0, r2, r3]),
                                      ])
def test_eval_input_parametrize(arg, ret):
    assert eval_input(arg) == ret
