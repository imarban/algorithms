class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        asarray = [c for row in matrix for c in row]

        return self.binarySearch(asarray, target)

    def binarySearch(self, array, target):

        first = 0
        last = len(array) - 1
        found = False

        while first <= last and not found:
            half = (last + first) / 2

            if array[half] == target:
                found = True

            else:
                if array[half] > target:
                    last = half - 1
                else:
                    first = half + 1

        return found


a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

print Solution().searchMatrix(a, 16)
