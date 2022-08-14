#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_none(obj):
    if obj:
        print('{obj} is not None'.format(obj=obj))
    else:
        print('{obj} is None'.format(obj=obj))

def main():
    check_none(None)
    check_none('Hello, World!')

if __name__ == '__main__':
    main()