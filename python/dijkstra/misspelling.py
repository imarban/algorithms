__author__ = 'igomez'

CAYLEY_TABLE = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
                'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
                'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
                'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}


class Quaternion(object):
    def __init__(self, value):
        self.negative = True if value[0] == '-' else False
        self.value = str(value[1:]) if self.negative else str(value)

    def __mul__(self, other):
        to_return = self

        if self.value == '1':
            to_return = other
        elif self.value == 'i':
            if other.value == '1':
                return self
            elif other.value == 'i':
                to_return = Quaternion('-1')
            elif other.value == 'j':
                to_return = Quaternion('k')
            elif other.value == 'k':
                to_return = Quaternion('-j')
        elif self.value == 'j':
            if other.value == '1':
                to_return = self
            elif other.value == 'i':
                to_return = Quaternion('-k')
            elif other.value == 'j':
                to_return = Quaternion('-1')
            elif other.value == 'k':
                to_return = Quaternion('i')
        elif self.value == 'k':
            if other.value == '1':
                to_return = self
            elif other.value == 'i':
                to_return = Quaternion('j')
            elif other.value == 'j':
                to_return = Quaternion('-i')
            elif other.value == 'k':
                to_return = Quaternion('-1')

        if (self.negative and other.negative) or (not self.negative and not other.negative):
            to_return.negative = False
        else:
            to_return.negative = True
        return to_return


quaternion_1_positivo = Quaternion('1')
quaternion_1_negativo = Quaternion('-1')
quaternion_i_positivo = Quaternion('i')
quaternion_i_negativo = Quaternion('-i')
quaternion_j_positivo = Quaternion('j')
quaternion_j_negativo = Quaternion('-j')
quaternion_k_positivo = Quaternion('k')
quaternion_k_negativo = Quaternion('-k')


def is_misspelled(word, size_of_word):
    if size_of_word < 2:
        return False
    for x in xrange(0, size_of_word):
        for y in xrange(x + 1, size_of_word):
            left = operate_word(word[0:y], y)
            if left == 'i':
                for z in xrange(y + 1, size_of_word):
                    middle = word[y:z]
                    right = word[z:]
                    if operate_word(middle, z - y) == 'j' and operate_word(right, size_of_word - z) == 'k':
                        print word[0:y], middle, right
                        return True

    return False


def operate_word(word, len_word):
    result = word[0]
    for i in xrange(1, len_word):
        result = mult(result, word[i])

    return result


def remove_sign(quat):
    return quat if quat[0] != '-' else quat[1:]


def mult(first, second):
    nosign1, nosign2 = remove_sign(first), remove_sign(second)

    result = CAYLEY_TABLE.get(nosign1).get(nosign2)

    if first[0] == '-' and result[0] == '-':
        return remove_sign(result)
    if (first[0] == '-' and second[0] != '-') or (first[0] != '-' and second[0] == '-'):
        return '-' + result
    return result


#
# if __name__ == '__main__':
#     with open("C-small-practice.in", "r") as inputfile:
#         test_cases = int(inputfile.readline())
#         word_size = inputfile.readline().split(" ")
#         word_size = int(word_size[0]) * int(word_size[1])
#
#         results = []
#         for i in xrange(1, 2):
#             read = inputfile.readline().strip()
#             results.append(
#                 "Case #{}: {}\n".format(i, "YES" if is_misspelled(read, word_size) else "NO"))
#
#         outputfile = open("output.out", "w")
#         outputfile.writelines(results)
#         outputfile.close()

print is_misspelled(
    "".join(["ijk" for _ in range(1, 11)]), 30)
