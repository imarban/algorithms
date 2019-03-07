def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)


sortit = [10, 6, 7, 2, 9, 11, 1, 0, 3]

quicksort(sortit, 0, len(sortit) - 1)

print sortit
