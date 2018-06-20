def find_words_util(board, dictionary, i, j, n, m, visited, letters):
    letters.append(board[i][j])
    word = ''.join(letters)
    if word in dictionary:
        print(word)
    
    visited[i][j] = True
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if k >= 0 and k < n and l >= 0 and l < m and not visited[k][l]:
                find_words_util(board, dictionary, k, l, n, m, visited, letters)
    
    del letters[-1]
    visited[i][j] = False


def find_words(board, dictionary, n, m):
    visited = []
    for i in range(n):
        visited.append([])
        for j in range(m):
            visited[i].append(False)

    for i in range(n):
        for j in range(m):
            find_words_util(board, dictionary, i, j, n, m, visited, [])




board = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]
dictionary = set(['GEEKS', 'FOR', 'QUIZ', 'GO'])

find_words(board, dictionary, 3, 3)