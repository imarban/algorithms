class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        results = {}

        for i in xrange(len(nums)):
            if nums[i] in results:
                return [results[nums[i]] + 1, i + 1]
            else:
                results[target - nums[i]] = i

        return []


print Solution().twoSum([2, 7, 11, 15], 9)
print Solution().twoSum([0, 4, 3, 0], 0)
print Solution().twoSum([-1, -2, -3, -4, -5], -8)
