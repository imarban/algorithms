__author__ = 'igomez'


# Traverse a matrix in clockwise
def snail(array):
    n = len(array)
    output = []

    for layer in xrange((n / 2) + 1):
        first = layer
        last = n - layer - 1

        output.extend(array[layer][first:last + 1])
        output.extend(array[row][last] for row in xrange(layer + 1, last))
        output.extend(array[last][last:first:-1])
        output.extend(array[row][first] for row in xrange(last, layer, -1))

    return output


array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def snail2(array):
    return list(array[0]) + snail2(zip(*array[1:])[::-1]) if array else []
