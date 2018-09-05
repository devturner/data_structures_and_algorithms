
def find_max_value(g_tree):
    """ given a binary tree, find the max value
        stored in that tree
    """
    if g_tree.root is None:
        return
    
    max_value = g_tree.root.value
    queue = []

    queue.append(g_tree.root)

    while (len(queue) > 0):
        node = queue.pop(0)
        if node.value > max_value:
            max_value = node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return max_value
