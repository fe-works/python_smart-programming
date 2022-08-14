#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NewStyleClass(object):
    pass

class OldStyleClass(object):
    pass

def print_attrs(class_):
    class_attrs = dir(class_)
    class_attrs_len = len(class_attrs)
    msg = '{class_name}: {attrs_len}'.format(
        class_name = class_.__name__,
        attrs_len = class_attrs_len,
    )

    print(msg)


def main():
    print_attrs(NewStyleClass)
    print_attrs(OldStyleClass)

if __name__ == '__main__':
    main()
