def find_unique(array):
    freqs = dict()
    for element in array:
        if element in freqs:
            freqs[element] += 1
        else:
            freqs[element] = 1

    for key, value in freqs.items():
        if value == 1:
            return key

    return -1


def find_unique_limited(array, bottom, top):
    expected_sum_bottom = (bottom - 1) * (bottom)
    expected_sum_top = top * (top + 1)
    expected_sum = expected_sum_top - expected_sum_bottom
    actual_sum = sum(array, 0)

    return expected_sum - actual_sum


def find_unique_hacky(array):
    from functools import reduce

    return reduce(lambda x, y: x ^ y, array)


# print(find_unique([1, 1, 4, 5, 5, 7, 6, 7, 6, 3, 3]))
#print(find_unique_limited([1, 1, 4, 4, 5, 5, 7, 6, 6, 3, 3, 2, 2, 8, 8], 1, 8))
print(find_unique_hacky([1, 1, 4, 4, 5, 5, 7, 6, 6, 3, 3, 2, 2, 8, 8]))
