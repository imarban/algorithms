"""

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

ABCCED = True
SEE = True
ABCB = False

"""
from algorithms.wordsearch import large


class Solution(object):
    found = False

    def is_out_edges(self, position):
        return position[0] > self.matrix_size[0] - 1 or position[0] < 0 or position[1] > self.matrix_size[1] - 1 or \
               position[1] < 0

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not len(board) or type(board[0]) is not list or not len(board[0]):
            return False

        self.matrix_size = (len(board), len(board[0]))

        for i in xrange(self.matrix_size[0]):
            for j in xrange(self.matrix_size[1]):
                operations = [(i, j)]
                visited = [[False] * self.matrix_size[1] for _ in xrange(self.matrix_size[0])]
                letter_index = 0

                while operations:
                    x, y = operations.pop()
                    if not self.is_out_edges((x, y)) and not visited[x][y] and board[x][y] == word[letter_index]:
                        letter_index += 1
                        visited[x][y] = True
                        operations.append((x - 1, y))  # top
                        operations.append((x, y + 1))  # right
                        operations.append((x + 1, y))  # bottom
                        operations.append((x, y - 1))  # left
                    if letter_index >= len(word):
                        return True

        return False


# print Solution().exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "SEE")
#
# print Solution().exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "ABCCED")
#
# print Solution().exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "ABCB")

print Solution().exist(large.a, "leniytflws")
