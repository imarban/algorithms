__author__ = 'igomez'


def replace(value):
    chars = list(value)
    for i in xrange(len(chars)):
        if ord(chars[i]) == 32:
            chars[i] = '%20'
    return "".join(chars)


print replace("This is a test")
