def kadane(values):
    max_so_far = values[0]
    max_here = values[0]

    for i in range(1, len(values)):
        max_here = max(values[i], max_here + values[i])
        max_so_far = max(max_so_far, max_here)
    
    return max_so_far
 


print(kadane([-4, -2, 1, -3]))
print(kadane([-1, 2, -3, 4]))
print(kadane([1, 1, 1, 1, 1, 1]))
print(kadane([10, -10]))
print(kadane([-10, -1]))
print(kadane([5, 7, -9, 3, -4, 2, 1, -8, 9, 10]))