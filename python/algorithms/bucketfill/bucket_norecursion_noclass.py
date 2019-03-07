"""
Function which detects if a position is out of the edge of the matrix
"""


def is_out_edges(matrix_size, position):
    return position[0] > matrix_size[0] - 1 or position[0] < 0 or position[1] > matrix_size[1] - 1 or position[1] < 0


"""
This functions modifies matrix in place. It uses a recursion stack to avoid recursive calls. It assumes that matrix is square.
"""


def fill(matrix, x, y, new_color):
    # Checking if matrix is not empty or if the new color is not the same as original color
    if not len(matrix) or not len(matrix[0]) or new_color == matrix[x][y]:
        return

    # Checking if position to change color is not out of matrix boundaries
    if is_out_edges([len(matrix), len(matrix[0])], (x, y)):
        return

    matrix_size = [len(matrix), len(matrix[0])]
    original = matrix[x][y]
    operations = [(x, y)]

    while len(operations):
        x, y = operations.pop()

        if not is_out_edges(matrix_size, [x, y]) and matrix[x][y] == original:
            operations.append((x - 1, y))  # top
            operations.append((x, y + 1))  # right
            operations.append((x + 1, y))  # bottom
            operations.append((x, y - 1))  # left

            matrix[x][y] = new_color


matrix_to_fill = [[1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 0],
                  [1, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0], ]

empty = [[]]

fill(matrix_to_fill, 2, 2, 5)

print matrix_to_fill
