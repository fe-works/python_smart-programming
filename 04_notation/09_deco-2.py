# !/usr/bin/env python
# -*- coding: utf-8 -*-

def clamp (func):
    """デコレータとして動作する関数"""

    def _clamp(*args, **kwargs):
        """デコレータが返す関数"""

        print('before Processing')

        result = func(*args, **kwargs)

        print('After processing')

        return result

    return _clamp

@clamp
def greet():
    print('Hello,World!')

def main():
    greet()

if __name__ == '__main__':
    main()