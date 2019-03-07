class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        j = 1
        k = 2

        while k < len(nums):
            if nums[j-1] != nums[j] or nums[j] != nums[k]:
                j += 1
                nums[j] = nums[k]
            k += 1

        return j + 1


a = [1, 1, 1, 2, 2, 3]
print Solution().removeDuplicates(a)
print a

a = [1, 2, 2]
print Solution().removeDuplicates(a)
print a
