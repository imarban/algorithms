class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # check base case
        return num - 9 * ((num - 1) / 9) if num > 0 else num


print Solution().addDigits(38)
