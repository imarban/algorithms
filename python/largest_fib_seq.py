# https://www.geeksforgeeks.org/largest-subset-whose-all-elements-are-fibonacci-numbers/

#code

import math

def is_perfect_square(number):
    root = int(math.sqrt(number))
    return root * root == number
    

def is_fib_number(number):
    return is_perfect_square((5*number*number) + 4) or is_perfect_square((5*number*number) - 4)
    
def get_largest_seq(values):
    
    return [value for value in values if is_fib_number(value)]
    

print(get_largest_seq([1, 4, 3, 9, 10, 13, 7]))
    