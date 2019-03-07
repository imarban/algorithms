class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        visited = {}
        operations = [n]

        while len(operations):
            num = operations.pop()

            if num == 1:
                return True

            result = 0
            while num > 9:
                result += (num % 10) ** 2
                num /= 10

            result += num ** 2

            if result not in visited:
                operations.append(result)
                visited[result] = True

            else:
                return False


print Solution().isHappy(110)
