class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return

        first = 0
        last = len(matrix) * len(matrix[0]) - 1
        found = False

        while first <= last and not found:
            half = (first + last) / 2
            halfx = half / len(matrix[0])
            halfy = half % len(matrix[0])

            if matrix[halfx][halfy] == target:
                found = True
            else:
                if matrix[halfx][halfy] > target:
                    last = half - 1
                else:
                    first = half + 1

        return found


a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

print Solution().searchMatrix(a, 30)
