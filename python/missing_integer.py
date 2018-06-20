def missing_integer(array):
    # write your code in Python 3.6
    freqs = [0] * 1000001
    for elem in array:
        if elem > 0:
            freqs[elem] += 1

    for i in range(1, len(freqs)):
        if freqs[i] == 0:
            return i


def missing_integer_better(array):
    if len(array) == 1:
        return array[0] + 1 if array[0] >= 0 else 1

    values = set()
    for elem in array:
        if elem > 0:
            values.add(elem)

    i = 1
    while i < len(array):
        if i not in values:
            return i
        i += 1

    return i + 1


print(missing_integer_better([-1, -5, 0, 1, 2, 3, 100000, 6, 4]))
print(missing_integer_better([1, 3, 6, 4, 1, 2]))
print(missing_integer_better([1, 2, 3, 4, 5, 10, 15]))
print(missing_integer_better([1, 2, 3]))
print(missing_integer_better([0]))
