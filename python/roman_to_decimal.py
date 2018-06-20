#https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

def convert_to_int(roman_number):
    result = 0
    
    values = {'X': 10, 'C': 100, 'V': 5, 'D': 500, 'L': 50, 'M': 1000, 'I': 1}
    value_decrease = {'I': set(['X', 'V']), 'C': set(['M', 'D']), 'X': set(['C', 'L'])}
    
    previous_char = None

    for i in range(len(roman_number) - 1, -1, -1):
        current_char = roman_number[i]
        if current_char in value_decrease and previous_char in value_decrease[current_char]:
            result -= values[current_char]
        else:
            result += values[current_char]
        previous_char = current_char
    
    return result
            


print(convert_to_int('MMMCMXCIX'))