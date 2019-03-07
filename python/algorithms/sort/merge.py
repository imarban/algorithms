def partition(to_sort):
    return to_sort[:len(to_sort) / 2], to_sort[len(to_sort) / 2:]


def merge(array1, array2):
    result = []

    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    if j < len(array2):
        result.extend(array2[j:])
    if i < len(array2):
        result.extend(array1[i:])

    return result


def mergesort(to_sort):
    if len(to_sort) == 1:
        return to_sort

    first_half, second_half = partition(to_sort)

    first_half = mergesort(first_half)
    second_half = mergesort(second_half)

    return merge(first_half, second_half)


print mergesort([10, 6, 7, 2, 9, 11, 1, 0, 3])
