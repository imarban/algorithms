__author__ = 'igomez'


def to_zero(matrix):
    matrix_copy = [[x for x in y] for y in matrix]

    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix_copy[i] = [0] * len(matrix[i])
                for k in xrange(len(matrix)):
                    matrix_copy[k][j] = 0

    return matrix_copy


def to_zero_quad(matrix):
    rows = [None] * len(matrix)
    columns = [None] * len(matrix[0])

    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == 0:
                rows[i] = True
                columns[j] = True

    for i in xrange(len(rows)):
        for j in xrange(len(columns)):
            if rows[i] or columns[j]:
                matrix[i][j] = 0

    return matrix


print to_zero_quad([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 0, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25],
                    ])
