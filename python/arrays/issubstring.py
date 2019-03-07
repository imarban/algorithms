__author__ = 'igomez'


def is_rotation(word1, word2):
    if len(word2) != len(word1):
        return False

    to_move = ''
    for i in xrange(len(word2)):
        if word2[i] != word1[0]:
            to_move += word2[i]
        else:
            break

    word2 = word2[i:] + to_move

    return word2 in word1


def is_rotation_one_liner(word1, word2):
    return len(word2) == len(word1) and word2 in word1 + word1


print is_rotation_one_liner("holatodos", "latodosho")
