__author__ = 'igomez'


def unique(value):
    counts = [0] * 128
    for c in value:
        if counts[ord(c)] != 0:
            return False
        counts[ord(c)] = 1
    return True


print unique("hola")
