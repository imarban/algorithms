def is_balanced(expression):
    braces = {'{': '}', '(': ')', '[': ']'}

    ops = []

    if not expression:
        return True

    for c in expression:
        if c in braces.keys():
            ops.append(c)
        elif is_closing_brace(c):
            op = ops.pop()
            if braces.get(op) != c:
                return False

    return True


def is_closing_brace(c):
    return ord(c) == 93 or ord(c) == 41 or ord(c) == 125


print is_balanced("[{a}]")
