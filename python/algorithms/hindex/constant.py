class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        equal_h = [0] * (n + 1)
        for h in range(n):
            if citations[h] >= n:
                equal_h[n] += 1
            else:
                equal_h[citations[h]] += 1

        s = 0
        for h in range(n, 0, -1):
            s += equal_h[h]
            if s >= h:
                return h

        return 0


print Solution().hIndex([3, 0, 6, 1, 5])
