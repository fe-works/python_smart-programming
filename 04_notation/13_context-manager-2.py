#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def context_manager():
    print('before processing')
    try:
        yield
    finally:
        print('After Processing')

def main():
    with context_manager():
        print('Hello, World!')

if __name__ == '__main__':
    main()