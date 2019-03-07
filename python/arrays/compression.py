__author__ = 'igomez'


def compression(value):
    results = []
    counter = 1
    for i in xrange(1, len(value)):
        if value[i] == value[i - 1]:
            counter += 1
        else:
            results.append(value[i - 1])
            results.append(str(counter))
            counter = 1

    results.append(value[i])
    results.append(str(counter))

    return "".join(results) if len(results) <= len(value) else value


print compression("aabcccccaaa")
