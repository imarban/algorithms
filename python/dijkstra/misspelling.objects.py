__author__ = 'igomez'


class QuaternionBuilder(object):
    @staticmethod
    def get_quaternion(value):
        negative = True if value[0] == '-' else False
        value = str(value[1:]) if negative else str(value)
        if negative:
            if value == '1': return quaternion_1_negativo
            if value == 'i': return quaternion_i_negativo
            if value == 'j': return quaternion_j_negativo
            if value == 'k': return quaternion_k_negativo
        else:
            if value == '1': return quaternion_1_positivo
            if value == 'i': return quaternion_i_positivo
            if value == 'j': return quaternion_j_positivo
            if value == 'k': return quaternion_k_positivo


class Quaternion(object):
    def __init__(self, value):
        self.negative = True if value[0] == '-' else False
        self.value = str(value[1:]) if self.negative else str(value)

    def __str__(self):
        return "-" + self.value if self.negative else self.value

    def __mul__(self, other):
        to_return = self

        if self.value == '1':
            to_return = other
        elif self.value == 'i':
            if other.value == '1':
                return self
            elif other.value == 'i':
                to_return = quaternion_1_negativo
            elif other.value == 'j':
                to_return = quaternion_k_positivo
            elif other.value == 'k':
                to_return = quaternion_j_negativo
        elif self.value == 'j':
            if other.value == '1':
                to_return = self
            elif other.value == 'i':
                to_return = quaternion_k_negativo
            elif other.value == 'j':
                to_return = quaternion_1_negativo
            elif other.value == 'k':
                to_return = quaternion_i_positivo
        elif self.value == 'k':
            if other.value == '1':
                to_return = self
            elif other.value == 'i':
                to_return = quaternion_j_positivo
            elif other.value == 'j':
                to_return = quaternion_i_negativo
            elif other.value == 'k':
                to_return = quaternion_1_negativo

        if (self.negative and to_return.negative) or (not self.negative and not to_return.negative):
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
    if size_of_word < 3:
        return False

    result_left = result_middle = quaternion_1_positivo

    for x in xrange(0, size_of_word):
        result_left *= QuaternionBuilder.get_quaternion(word[x])
        if result_left.value == 'i' and not result_left.negative:
            for y in xrange(x + 1, size_of_word):
                result_middle *= QuaternionBuilder.get_quaternion(word[y])
                if result_middle.value == 'j' and not result_middle.negative:
                    return True

    return False


def operate_word(word, len_word):
    result = QuaternionBuilder.get_quaternion(word[0])
    for z in xrange(1, len_word):
        result *= QuaternionBuilder.get_quaternion(word[z])
    return result


# if __name__ == '__main__':
#     with open("C-small-practice.in", "r") as inputfile:
#         test_cases = int(inputfile.readline())
#
#         results = []
#         for case in xrange(1, test_cases + 1):
#             sizes = map(int, inputfile.readline().split(" "))
#             read = inputfile.readline().strip()
#             string = read * sizes[1]
#             result_reduce_to_minus = operate_word(string, sizes[0] * sizes[1])
#
#             print case
#             if str(result_reduce_to_minus) != '-1':
#                 results.append(
#                     "Case #{}: {}\n".format(case, "NO"))
#             else:
#                 results.append(
#                     "Case #{}: {}\n".format(case,
#                                             "YES" if is_misspelled(read * sizes[1], sizes[0] * sizes[1]) else "NO"))
#
#         outputfile = open("output.out", "w")
#         outputfile.writelines(results)
#         outputfile.close()

string = "i" * 10000
# print operate_word(string, len(string))
print is_misspelled(string, len(string))
