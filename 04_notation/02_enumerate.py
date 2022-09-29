#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    array = ['foo', 'bar', 'baz']
    for index, value in enumerate(array):
        print('{index} : {value}'.format(index=index, value=value))

if __name__ == '__main__':
    main()