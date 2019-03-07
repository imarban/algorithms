__author__ = 'igomez'


def minimum_frieds(people):
    claps = friends = 0
    for idx, item in enumerate(people):
        if idx > claps:
            friends += idx - claps
            claps += idx - claps
        claps += item

    return friends


if __name__ == '__main__':
    with open("A-small-practice.in", "r") as inputfile:
        test_cases = int(inputfile.readline())

        results = []
        for i in xrange(1, test_cases + 1):
            read = inputfile.readline().strip().split(" ")
            results.append(
                ("Case #{}: {}\n".format(i, minimum_frieds([int(d) for d in read[1]]))))

        outputfile = open("output.out", "w")
        outputfile.writelines(results)
        outputfile.close()
