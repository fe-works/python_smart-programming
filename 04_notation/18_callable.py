#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable


class CallableClass(object):
    def __call__ (self, msg):
        print(msg)

def main():
    obj = CallableClass()
    obj('Hello, world!')

if __name__ == '__main__':
    main()