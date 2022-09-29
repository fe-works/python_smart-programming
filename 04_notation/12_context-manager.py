#!usr/bin/env python
# -*- coding: utf-8 -*-

class ContextManager(object):
    def __enter__(self):
        print('before processing')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('after Processing')

def main():
    with ContextManager():
        print('Hello, world!')

if __name__ == '__main__':
    main()
