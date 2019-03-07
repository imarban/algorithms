class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        i = len(nums) - 2
        p = 0

        while i >= 0 and not p:
            if nums[i] < nums[i + 1]:
                p = i
                break
            i -= 1

        i = len(nums) - 1
        q = 0

        while i >= 0 and not q:
            if nums[i] > nums[p]:
                q = i
                break
            i -= 1

        if p == 0 and q == 0:
            nums.sort()
            return

        nums[p], nums[q] = nums[q], nums[p]

        left = p + 1
        right = len(nums) - 1

        while left <= right:
            aux = nums[right]
            nums[right] = nums[left]
            nums[left] = aux

            left += 1
            right -= 1


a = [3, 2, 1]
Solution().nextPermutation(a)
print a
