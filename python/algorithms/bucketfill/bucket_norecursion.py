def is_out_edges(matrix_size, positions):
    return positions[0] > matrix_size[0] - 1 or positions[0] < 0 or positions[1] > matrix_size[1] - 1 or positions[
                                                                                                             1] < 0


class OperationBucketFill(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def fill(matrix, x, y, new_color):
    matrix_size = [len(matrix), len(matrix[0])]
    original = matrix[x][y]
    operations = [OperationBucketFill(x, y)]

    while len(operations):
        operation = operations.pop()
        matrix[operation.x][operation.y] = new_color

        # top
        if not is_out_edges(matrix_size, [operation.x - 1, operation.y]) and matrix[operation.x - 1][
            operation.y] == original:
            operations.append(OperationBucketFill(operation.x - 1, operation.y))

        # right
        if not is_out_edges(matrix_size, [operation.x, operation.y + 1]) and matrix[operation.x][
                    operation.y + 1] == original:
            operations.append(OperationBucketFill(operation.x, operation.y + 1))

        # bottom
        if not is_out_edges(matrix_size, [operation.x + 1, operation.y]) and matrix[operation.x + 1][
            operation.y] == original:
            operations.append(OperationBucketFill(operation.x + 1, operation.y))

        # left
        if not is_out_edges(matrix_size, [operation.x, operation.y - 1]) and matrix[operation.x][
                    operation.y - 1] == original:
            operations.append(OperationBucketFill(operation.x, operation.y - 1))


matrix_to_fill = [[0, 0, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 1, 0, 0], ]

fill(matrix_to_fill, 2, 2, 5)

print matrix_to_fill
