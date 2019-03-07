__author__ = 'igomez'


def rotate(matrix, n):
    for layer in xrange(n / 2):
        first = layer
        last = n - layer - 1

        for i in xrange(first, last):
            offset = i - first
            top = matrix[first][i]
            # left->top
            matrix[first][i] = matrix[last - offset][first]
            # bottom->left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right->bottom
            matrix[last][last - offset] = matrix[last - offset][last]
            # top->right
            matrix[i][last] = top

    return matrix


print rotate([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              ], 5)
