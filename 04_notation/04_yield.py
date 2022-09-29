#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

def myGenerator(stop, start=0):
    current_value = start

    while True:
        if current_value >= stop:
            break
        yield current_value

        current_value += 1
    
def main():
    it = myGenerator(10)
    for i in it:
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()