from algorithms.gas_station import input


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if len(gas) != len(cost):
            return False

        if sum(gas) < sum(cost):
            return False

        start_gas = 0
        number_gas_stations = len(gas)

        while start_gas < len(gas):
            current = start_gas
            gas_av = 0
            can_continue = True

            while current != start_gas - 1 and can_continue:
                # Filling the tank
                gas_av += gas[current]
                # Subtracting fuel spent
                gas_av -= cost[current]

                # Checking if end of array is reached
                current = current + 1 if current + 1 < number_gas_stations else -1

                # Checking out of fuel for next movement
                if gas_av < 0:
                    can_continue = False

            if gas_av >= 0:
                return start_gas

            start_gas += 1

        return start_gas


gas = [10, 5, 1, 7, 0, 9, 2, 8, 1]
cost = [7, 3, 1, 6, 2, 9, 1, 2, 3]

print Solution().canCompleteCircuit(input.gas, input.cost)
