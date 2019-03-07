class Solution(object):
    def check_index(self, array, h):
        with_split = array[:h]
        without_split = array[h:]

        for i in with_split:
            if i < h:
                return False

        for i in without_split:
            if i > h:
                return False

        return True

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations:
            return 0

        citations.sort(reverse=True)

        for k in xrange(len(citations), -1, -1):
            if self.check_index(citations, k):
                return k


print Solution().hIndex([])
