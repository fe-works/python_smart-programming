#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

class SuperClass(metaclass=abc.ABCMeta):
    def greet(self):
        print('Super')

class DuckSubClass(object):
    def greet(self):
        print('sub')

SuperClass.register(DuckSubClass)

def main():
    obj = DuckSubClass()
    print(isinstance(obj, SuperClass))

if __name__ == '__main__':
    main()