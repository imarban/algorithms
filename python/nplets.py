def find_pairs(array, sum):
    values_index = dict()

    for i in range(0, len(array)):
        values_index[array[i]] = i

    tuples = []
    for i in range(0, len(array)):
        element = array[i]
        toFind = sum - element
        if toFind in values_index and values_index[toFind] > i:
            tuples.append((element, toFind))

    return tuples


def find_triplets(array, sum):
    triplets = []
    for i in range(0, len(array)):
        pairs = find_pairs(array[i:], sum - array[i])
        for j in range(i, len(pairs)):
            triplets.append((array[i], pairs[j][0], pairs[j][1]))

    print(triplets)


def build_pairs(array):
    sums = dict()
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            if sum in sums:
                sums[sum].append((array[i], array[j]))
            else:
                sums[sum] = [(array[i], array[j])]

    return sums


print(find_triplets([1, 1, 2, 3, 4, 5, 6], 6))

def find_nplets(array, sum, N):
    combinations = build_pairs(array)
    results = []

    if N % 2 == 0:
        pairs = find_pairs(list(combinations.keys()), sum)

        for pair in pairs:
            pass
            # result = [val +  for val in combinations[pair[0]]]
            # print(result)
            # results.append(result)



#find_nplets([5, 4, 8, 1, 7, 3], 14, 4)