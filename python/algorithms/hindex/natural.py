class Solution(object):
    def check_index(self, array, h):
        without_split = array[:len(array) - h]
        with_split = array[len(array) - h:]

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

        citations.sort()
        maxk = 0

        for k in xrange(0, len(citations)):
            if self.check_index(citations, k):
                maxk = k

        return maxk


print Solution().hIndex([1,0])
