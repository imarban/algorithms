# https://www.geeksforgeeks.org/convert-ternary-expression-binary-tree/

class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traverse_tree_preorder(node, values):
    if node:
        values.append(node.data)
        traverse_tree_preorder(node.left, values)
        traverse_tree_preorder(node.right, values)


def get_tree_from_ternary_util(ternary_expression, node, prev_char, index):
    if index >= len(ternary_expression):
        return
    char = ternary_expression[index]
    if char == '?' or char == ':':
        get_tree_from_ternary_util(ternary_expression, node, char, index + 1)
    else:
        if prev_char == '?':
            node.left = Node(char)
            get_tree_from_ternary_util(ternary_expression, node.left, char, index + 1)
        elif prev_char == ':':
            node.right = Node(char)
            get_tree_from_ternary_util(ternary_expression, node.right, char, index + 1)

    

def get_tree_from_ternary(ternary_expression):
    tree = Node(ternary_expression[0])
    get_tree_from_ternary_util(ternary_expression, tree, ternary_expression[0], 1)
    values = []
    traverse_tree_preorder(tree, values)
    return values



print(get_tree_from_ternary('a?b:c'))
print(get_tree_from_ternary('a?b?c:d:e'))