#!usr/bin/env python
# -*- coding: utf-8 -*-


# @register デコレータで登録した関数の整理
_HANDLERS = {}

def register(func):
    """修飾した関数を _HANDLERS に登録"""
    func_name = func.__name__
    _HANDLERS[func_name] = func

    return func

@register
def greet():
    print('Hello, World!')

def call(name):
    func = _HANDLERS.get(name)
    func()

def main():
    call('greet')

if __name__ == '__main__':
    main()