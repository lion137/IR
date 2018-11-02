#! /home/lion/anaconda3/bin/python
# main program

from inverted_index_class import *


def prompt(p="enter query > "):
    while True:
        try:
            val = input(p)
            print(eval_input(val))
        except ValueError:
            print("Incorrect format, try again")
            continue
        else:
            continue

if __name__ == '__main__':
    prompt()



