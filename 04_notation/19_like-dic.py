#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

class MyDict(object):
    """辞書ライクなインタフェを持つ"""

    def __init__ (self):
        self._dict = {}

    def __setitem__(self, key, value):
        """self[key] = value するときに呼ばれる"""
        self._dict[key] = value

    def __getitem__ (self, key):
            """del self[key] するときに呼ばれる"""
            return self._dict[key]

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, key):
        """key in self するときに呼ばれる"""
        return key in self._dict

    def __len__(self):
        """len(self)するときに呼ばれる"""
        return len(self._dict)

    def __getattr__(self, name):
        return getattr(self._dict, name)

def main():
    obj=MyDict()
    obj['greet']='Hello,World!'
    result='greet' in obj
    print('\'greet\'inobj:{result}'.format(result=result))
    result=obj['greet']
    print('obj[\'greet\']:{result}'.format(result=result))
    result=obj.get('greet')
    print('obj.get(\'greet\'):{result}'.format(result=result))
    del obj['greet']
    result=len(obj)
    print('len(obj):{result}'.format(result=result))

if __name__ =='__main__':
    main()
