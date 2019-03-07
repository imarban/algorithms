__author__ = 'igomez'


def closest(array, target):
    start = 0
    end = len(array) - 1

    while end - start != -1:
        half = (end + start) / 2

        if array[half] == target:
            return half

        if array[half] > target:
            end = half - 1
        else:
            start = half + 1

    return end if target - array[end] > target - array[start] else start


print closest([1.1, 1.2751, 1.321, 2.421, 3.017], 1.30)
