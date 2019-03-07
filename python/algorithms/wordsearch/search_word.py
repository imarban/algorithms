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
square = lambda x: x*2

class Solution(object):
    found = False

    def is_out_edges(self, position):
        return position[0] > self.matrix_size[0] - 1 or position[0] < 0 or position[1] > self.matrix_size[1] - 1 or \
               position[1] < 0

    def check_letter(self, letter_index, row, column):
        if self.found:
            return

        if not self.is_out_edges((row, column)):

            if self.visited[row][column]:
                return

            self.visited[row][column] = True

            if self.word[letter_index] == self.board[row][column]:
                letter_index += 1

                if letter_index >= len(self.word) - 1:
                    self.found = True

                self.check_letter(letter_index, row - 1, column, )  # top
                self.check_letter(letter_index, row, column + 1, )  # right
                self.check_letter(letter_index, row + 1, column, )  # down
                self.check_letter(letter_index, row, column - 1)  # left

                return self.found

            else:
                return False
        else:
            return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if type(board[0]) is not list:
            return False

        if not len(board) or type(board[0]) is not list or not len(board[0]):
            return False

        self.matrix_size = (len(board), len(board[0]))
        self.board = board
        self.word = word
        self.found = False
        self.visited = [[False] * self.matrix_size[1] for _ in xrange(self.matrix_size[0])]

        for i in xrange(self.matrix_size[0]):
            for j in xrange(self.matrix_size[1]):
                if self.check_letter(0, i, j):
                    return True

        return False


print Solution().exist([['a']], "ab")
