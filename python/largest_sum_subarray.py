# https://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/

flatten = lambda l: [item for sublist in l for item in sublist]

def get_largest_sum(values, k):
    sums = [0] * (len(values) - k + 1)
    for i in range(len(values)):
        sums_limit = min(i + 1, len(sums))
        for j in range(sums_limit):
            if i - k == j:
                sums[j] = [sums[j], sums[j] + values[i]]
            elif i - k > j:
                sums[j].append(sums[j][-1] + values[i])
            else:
                sums[j] += values[i]
    
    sums[-1] = [sums[-1]]
    
    return max(flatten(sums))


print(get_largest_sum([-4, -2, 1, -3], 2))
print(get_largest_sum([-1, 2, -3, 4], 3))
print(get_largest_sum([1, 1, 1, 1, 1, 1], 2))
print(get_largest_sum([10, -10], 1))
print(get_largest_sum([5, 7, -9, 3, -4, 2, 1, -8, 9, 10], 5))