__author__ = 'igomez'


def count(value):
    counter = [0] * 256

    for c in value:
        counter[ord(c)] += 1

    return counter


def is_permutation(value1, value2):
    count1 = count(value1)
    count2 = count(value2)

    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True


print is_permutation("holaa", "aloha")
