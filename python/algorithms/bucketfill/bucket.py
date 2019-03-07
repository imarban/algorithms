def is_out_edges(matrix_size, positions):
    return positions[0] > matrix_size[0] - 1 or positions[0] < 0 or positions[1] > matrix_size[1] - 1 or positions[1] < 0


def fill(matrix, x, y, new_color):
    matrix_size = [len(matrix), len(matrix[0])]

    original = matrix[x][y]
    matrix[x][y] = new_color

    # top
    if not is_out_edges(matrix_size, [x - 1, y]) and matrix[x - 1][y] == original:
        fill(matrix, x - 1, y, new_color)
        matrix[x - 1][y] = new_color

    # right
    if not is_out_edges(matrix_size, [x, y + 1]) and matrix[x][y + 1] == original:
        fill(matrix, x, y + 1, new_color)
        matrix[x][y + 1] = new_color
    # bottom
    if not is_out_edges(matrix_size, [x + 1, y]) and matrix[x + 1][y] == original:
        fill(matrix, x + 1, y, new_color)
        matrix[x + 1][y] = new_color

    # left
    if not is_out_edges(matrix_size, [x, y - 1]) and matrix[x][y - 1] == original:
        fill(matrix, x, y - 1, new_color)
        matrix[x][y - 1] = new_color


matrix_to_fill = [[0, 0, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 1, 0, 0], ]

fill(matrix_to_fill, 2, 2, 5)

print matrix_to_fill
