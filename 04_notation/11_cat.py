#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cat(filename):
    with open(filename) as fp:
        lines = fp.readlines()
        print(lines)

    # 自動でclose()

    # OSを使う例
    # fp = open(filename)
    # try:
    #     lines = fp.readlines()
    #     print(lines)
    # finally:
    #     if fp is not None:
    #         fp.close()

def main():
    cat('sample.txt')

if __name__ == '__main__':
    main()
