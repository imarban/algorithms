def find_pairs_k(array, k):
    modulus_count = [0] * k
    for i in range(0, len(array)):
        modulus_count[array[i] % k] += 1

    count = int(modulus_count[0] * (modulus_count[0] - 1) / 2)
    for i in range(1, k // 2 + 1):
        if i == k / 2:
            count += int(modulus_count[i] * ((modulus_count[i] - 1) / 2))
        else:
            count += modulus_count[k - i] * modulus_count[i]

    return count


print(find_pairs_k([3, 5, 2, 1, 8, 9, 5], 10))
print(find_pairs_k([1, 3, 2, 6, 4, 5, 9], 3))
print(find_pairs_k([3, 5, 2, 1, 8, 9, 5, 5, 15], 10))
