def find_triplets(array, number):
    pairs = build_pairs(array)
    triplets = []

    used_indices_tuples = set()
    for i in range(0, len(array)):
        difference = number - array[i]
        if difference in pairs:
            pairs_to_get_sum = pairs[difference]

            for k in range(0, len(pairs_to_get_sum)):
                first_entry, second_entry = pairs_to_get_sum[k]
                triplet = (array[i], first_entry.value, second_entry.value)
                triplet_indices = tuple(sorted([i, first_entry.position, second_entry.position]))
                if triplet_indices not in used_indices_tuples and i != first_entry.position \
                        and i != second_entry.position:
                    triplets.append(triplet)
                    used_indices_tuples.add(triplet_indices)

    return triplets


def build_pairs(array):
    pairs = dict()

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            pair = (Entry(array[i], i), Entry(array[j], j))
            value = array[i] + array[j]

            if value in pairs:
                pairs[array[i] + array[j]].append(pair)
            else:
                pairs[array[i] + array[j]] = [pair]

    return pairs


class Entry:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __repr__(self):
        return "(" + str(self.value) + ", " + str(self.position) + ")"


print(find_triplets([1, 1, 2, 3, 4, 5, 6], 6))
print(find_triplets([1, 2, 3, 4, 5, 6, 12], 12))
