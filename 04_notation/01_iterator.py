#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

class MyIterator(object):
    """"連続した整数を返すイテレータクラス"""

    def __init__(self, stop=-1, start=0): # ここはどういう意味がある？start, stopとは？
        self.stop = stop
        self._current = start

    def __iter__ (self):
        """イテレータオブジェクトを返す"""
        return self

    def __next__(self):
        """次に取り出す要素を返す"""

        if self._current >= self.stop:
            raise StopIteration()
        result = self._current
        self._current += 1
        return result

    def next(self):
        """Python2.x系の代替関数"""
        return self.__next__()

def main():
    it = MyIterator(10)
    for i in it:
        print(i, end='')
    print()

if __name__ == '__main__':
    main()