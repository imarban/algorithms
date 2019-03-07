class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.matrix = matrix
        max_square = 0

        for i in xrange(len(matrix)):
            for j in range(len(matrix[i])):
                size = self.check_square(i, j)
                if size > max_square:
                    max_square = size

        return max_square ** 2

    def check_square(self, x, y):
        j = 0

        while y + j < len(self.matrix[x]) and self.matrix[x][y + j] == 1:
            j += 1
        j -= 1
        size = j - 1

        for i in range(x + 1, len(self.matrix)):
            for k in range(y, j):
                if self.matrix[i][k] != 1:
                    return 1

        return size


print Solution().maximalSquare([[1, 1, 1, 0, 0, 1],
                                [1, 1, 1, 0, 0, 1],
                                [1, 1, 1, 0, 0, 1],
                                [0, 0, 0, 1, 0, 1], ])
