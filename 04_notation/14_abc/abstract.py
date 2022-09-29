#!usr/bin/env python
# -*- coding: utf-8 -*-

import abc

class SuperClass(metaclass=abc.ABCMeta):
    """抽象基底クラス"""

    @abc.abstractmethod
    def greet(self):
        """抽象メソッド"""
        pass

class SubClass(SuperClass):
    """具象クラス"""

    def greet(self):
        """具象メソッド"""
        print('Hello,World!')

def main():
    obj = SubClass()
    obj.greet()

# def main():
#     SuperClass()

if __name__ == '__main__':
    main()