#!/usr/bin/env python
# -*- coding: utf-8 -*-

def evens(n):
    
    # OLD
    # result = []

    # for i in range(n+1):
    #     if i%2 == 0:
    #         result.append(i)

    return [
            i
            for i in range(n + 1)
            if i % 2 == 0
            ]
    # return result

def main():
    list_ = evens(10)
    print(list_)

if __name__ == '__main__':
    main()
