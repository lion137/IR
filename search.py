#! /home/lion/anaconda3/bin/python
# main program

from imports import *

import inverted_index_class as inc
import inverted_index_functions as inf
from texts import *

text = inc.InvertedIndex(docs)
ind = text.data_index

def prompt(p="enter query > "):
    while True:
        try:
            val = input(p)
            print(inf.eval_input(val))
        except ValueError:
            print("Incorrect format, try again")
            continue
        else:
            break

if __name__ == '__main__':
    prompt()

