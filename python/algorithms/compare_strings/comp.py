def compare_manual(string1, string2):
    min_length = min(len(string1), len(string2))

    for i in xrange(min_length):
        if string1[i] != string2[i]:
            if string1[i] < string2[i]:
                return -1
            else:
                return 1

    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    else:
        return 0


print compare_manual("ab", "z")
