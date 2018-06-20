def max_tip(array1, array2, max1, max2):
    differences = [()] * len(array1)
    for i in range(0, len(array1)):
        differences[i] = (abs(array1[i] - array2[i]), i, 1 if array1[i] > array2[i] else 2)

    differences = sorted(differences, key=lambda element: element[0], reverse=True)

    sum_max1 = 0
    sum_max2 = 0

    max_tip_value = 0
    for i in range(0, len(array1)):
        _, position, waiter = differences[i]
        if waiter == 1:
            if sum_max1 < max1:
                max_tip_value += array1[position]
                sum_max1 += 1
            else:
                max_tip_value += array2[position]
                sum_max2 += 1
        else:
            if sum_max2 < max2:
                max_tip_value += array2[position]
                sum_max2 += 1
            else:
                max_tip_value += array1[position]
                sum_max1 += 1

    return max_tip_value


print(max_tip([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 3, 3))


print(max_tip([1, 4, 1], [2, 5, 3], 2, 1))
print(max_tip([1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8], 4, 4))

