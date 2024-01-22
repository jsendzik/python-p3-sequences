#!/usr/bin/env python3

def print_fibonacci(length):
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    if length == 0:
        list.clear()
        print(list)
    else:
        print(list[0:length])