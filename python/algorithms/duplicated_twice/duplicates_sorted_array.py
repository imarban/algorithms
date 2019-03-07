class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        values = {num: 0 for num in nums}

        for i in xrange(len(nums)):
            if values[nums[i]] < 2:
                values[nums[i]] += 1

        results = []
        prev = None

        for num in nums:
            if prev != num:
                results.extend([num] * values.get(num))
            prev = num

        count = sum(v for k, v in values.items())

        for i in xrange(count):
            nums[i] = results[i]

        return count


a = [1, 1, 1, 2, 2, 3]
print Solution().removeDuplicates(a)
print a
