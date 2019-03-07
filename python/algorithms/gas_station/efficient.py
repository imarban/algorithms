from algorithms.gas_station import input


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if len(gas) != len(cost):
            return -1

        if sum(gas) < sum(cost):
            return -1

        sum_remaining = 0
        total = 0
        start = 0

        for i in xrange(len(gas)):
            remaining = gas[i] - cost[i]

            if sum_remaining >= 0:
                sum_remaining += remaining
            else:
                sum_remaining = remaining
                start = i

            total += remaining

        return start if total >= 0 else -1


gas = [10, 5, 1, 7, 0, 9, 2, 8, 1]
cost = [7, 3, 1, 6, 2, 9, 1, 2, 3]

print Solution().canCompleteCircuit([4], [5])
