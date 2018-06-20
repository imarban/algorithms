def can_visit(matrix, i, j, n, m, visited):
    is_bounds = i < n and j < m and i > -1 and j > -1
    return is_bounds and matrix[i][j] == 1 and visited[i][j] == 0

def print_matrix(matrix):
    for row in matrix:
        print(row)

def find_objects_util(matrix, i, j, visited, n, m):
    visited[i][j] = 1

    # right
    if can_visit(matrix, i, j + 1, n, m, visited):
        find_objects_util(matrix, i, j + 1, visited, n, m)
    
    # down
    if can_visit(matrix, i + 1, j, n, m, visited):
        find_objects_util(matrix, i + 1, j, visited, n, m)

    # left
    if can_visit(matrix, i, j - 1, n, m, visited):
        find_objects_util(matrix, i, j - 1, visited, n, m)
    
    # up
    if can_visit(matrix, i - 1, j, n, m, visited):
        find_objects_util(matrix, i - 1, j, visited, n, m)

def find_objects(matrix, n, m):
    visited = []
    for i in range(n):
        visited.append([])
        for j in range(m):
            visited[i].append(0)

    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] != 1:
                find_objects_util(matrix, i, j, visited, n, m)
                result += 1

    return result
    
matrix = [[0,0,0,1,1], [0,1,1,0,0], [0,0,1,1,0], [1,1,0,1,0], [1,1,0,0,0]]
result = find_objects(matrix, 5, 5)
assert result == 3

matrix = [[0,0,0,1,1], [0,0,0,0,0], [0,0,1,1,0], [0,0,0,0,0], [1,1,0,0,0]]
result = find_objects(matrix, 5, 5)
assert result == 3

