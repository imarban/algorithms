def partition(to_sort):
    return to_sort[:len(to_sort) / 2], to_sort[len(to_sort) / 2:]


def merge(to_sort, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            to_sort[k] = left[i]
            i += 1
        else:
            to_sort[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        to_sort[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        to_sort[k] = right[j]
        j += 1
        k += 1


def mergesort(to_sort):
    if len(to_sort) == 1:
        return to_sort

    first_half, second_half = partition(to_sort)

    mergesort(first_half)
    mergesort(second_half)

    return merge(to_sort, first_half, second_half)


sortit = [10, 6, 7, 2, 9, 11, 1, 0, 3]

mergesort(sortit)

print sortit
