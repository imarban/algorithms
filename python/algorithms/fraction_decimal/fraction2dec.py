class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""

        result = []

        if numerator < 0 ^ denominator < 0:
            result += "-"

        numerator, denominator = abs(numerator), abs(denominator)

        result.append(str(numerator / denominator))

        remainder = numerator % denominator * 10
        if remainder == 0:
            return "".join(result)

        remainders = {}
        result.append(".")

        while remainder != 0:
            if remainder in remainders:
                beg = remainders.get(remainder)
                part1 = result[:beg]
                part1.append("(")
                part2 = result[beg:]
                part2.append(")")

                return "".join(part1 + part2)

            remainders[remainder] = len(result)
            result.append(str(remainder / denominator))
            remainder = remainder % denominator * 10

        return "".join(result)


print Solution().fractionToDecimal(1, 7)
