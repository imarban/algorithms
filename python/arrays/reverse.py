__author__ = 'igomez'


def reverse(value):
    if len(value) == 1:
        return value
    return reverse(value[1:]) + value[0]


def reverse_iter(value):
    result = []
    for i in xrange(len(value) - 1, -1, -1):
        result.append(value[i])
    return "".join(result)


def reverse_in_place(value):
    value = list(value)
    start, end = 0, len(value) - 1

    while start < end:
        value[start], value[end] = value[end], value[start]
        start += 1
        end -= 1

    return "".join(value)


def reverse_one_liner(value):
    return value[::-1]


print reverse_in_place("israel")
