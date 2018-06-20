# https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

def count_decoding_messages(message, n):         
        # A table to store results of subproblems
    count = [0] * (n+1) 
    count[0] = 1
    count[1] = 1
 
    for i in range(2, n+1):
     
        count[i] = 0

        if (message[i-1] > '0'):
            count[i] = count[i-1]
 
        if (message[i-2] == '1' or (message[i-2] == '2' and message[i-1] < '7') ):
            count[i] += count[i-2]
     
    return count[n]

 
print(count_decoding_messages("123", 3))
print(count_decoding_messages("2222", 4))
print(count_decoding_messages("222222", 6))
print(count_decoding_messages("22222222", 8))