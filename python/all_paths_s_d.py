def print_path_util(matrix, s, d, visited, partial_path):
    visited.add(s)
    if s == d:
        print('->'.join(partial_path))
        del partial_path[-1]
        return

    for i in range(len(matrix[s])):
        v = matrix[s][i]
        if v == 1 and i not in visited:
            partial_path.append(str(i))
            print_path_util(matrix, i, d, visited, partial_path)
            visited.remove(i)
    
    del partial_path[-1]

def print_paths(matrix, s, d, n, m):
    visited = []
    for i in range(n):
        visited.append([])
        for j in range(m):
            visited.append(False)
    
    visited = set()
    print_path_util(matrix, s, d, visited, [str(s)])


adj_matrix = [[0,1,1,1], [0,0,0,1], [1,1,0,0], [0,0,0,0]]
print_paths(adj_matrix, 2, 3, 4, 4)
print("-------")
adj_matrix = [[0,1,0,1,1], [0,0,1,1,0], [0,0,0,0,1], [0,0,0,0,0],[0,1,0,0,0]]
print_paths(adj_matrix, 0, 3, 5, 5)