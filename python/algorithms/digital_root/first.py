class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # check base case
        operations = [num]

        result = 0
        while len(operations):
            num = operations.pop()

            if num < 10:
                return num

            result = 0
            while num > 9:
                result += num / 10
                num %= 10

            result += num
            operations.append(result)

        return result


print Solution().addDigits(38)
