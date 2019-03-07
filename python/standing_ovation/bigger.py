__author__ = 'igomez'


def next_bigger(n):
    chs = [c for c in str(n)]

    if len(chs) < 2 or len(set(chs)) == 1: return -1

    for i in xrange(len(chs) - 1, 0, -1):
        if chs[i] == '0':
            chs[i], chs[i - 1] = chs[i - 1], chs[i]
        elif chs[i] > chs[i - 1]:
            chs[i], chs[i - 1] = chs[i - 1], chs[i]
            return int(''.join(chs))


def next_bigger2(n):
    found = False
    sumand = n
    n_sorted = sorted(str(n))

    while not found:
        sumand += 1
        found = n_sorted == sorted(str(sumand))

    return sumand


print next_bigger2(9876543210)
