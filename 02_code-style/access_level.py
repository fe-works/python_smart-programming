#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アンダーバーがあるので，外部からのアクセスは出来ない
def _private_function():
    return 'Hello, world!'

# アンダーバーがないので，外部からのアクセスを許す
def main():
    print(_private_function)

if __name__ == '__main__':
    main()