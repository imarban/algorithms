import sys

__author__ = 'igomez'


def infinite_house(pancakes):
    optimal = new_solution = max(pancakes)
    print pancakes,
    j = 1
    while new_solution-1 <= optimal:
        optimal = new_solution
        pancakes = generate_new(pancakes)
        new_solution = max(pancakes) + j
        j += 1

    print optimal
    return optimal


def generate_new(pancakes):
    pancakes = pancakes[:]
    max1 = max(pancakes)
    pancakes.remove(max1)
    pancakes.extend([max1 / 2, max1 / 2] if max1 % 2 == 0 else [max1 / 2, max1 / 2 + 1])

    return pancakes


if __name__ == '__main__':
    # with open("B-small-practice.in", "r") as inputfile:
    #     test_cases = int(inputfile.readline())
    #
    #     results = []
    #     for i in xrange(1, test_cases + 1):
    #         inputfile.readline()
    #         read = map(int, inputfile.readline().strip().split(" "))
    #
    #         results.append("Case #{}: {}\n".format(i, infinite_house(read)))
    #
    #     outputfile = open("output.out", "w")
    #     outputfile.writelines(results)
    #     outputfile.close()

    print infinite_house([4, 8, 7, 8, 3])
