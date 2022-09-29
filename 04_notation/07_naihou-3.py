#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dict_ = {i: chr(i) for i in range(ord('a'), ord('f')+1)}
    print(dict_)

    g = (i for i in range(10+1) if i % 2 == 0)
    list_ = list(g)
    print(g)
    print(list_)


    # filterを用いて書くと
    list_ = filter(lambda x: x % 2 == 0, range(10+1))

    # 内包表記
    list_ = [i for i in range(10+1) if i % 2 == 0]
    print(list_)

    # mapを使って書くと
    list_ = map(lambda x: x*2, range(10+1))

    # 内包表記
    list_ = [i*2 for i in range(10+1)]
    print(list_)