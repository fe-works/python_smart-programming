#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    @classmethod
    def greet(cls):
        print('Hello, world!')

def main():
    MyClass.greet()

if __name__ == '__main__':
    main()