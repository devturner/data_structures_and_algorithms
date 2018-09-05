
def breadth_first_traversal(g_tree):

    if g_tree.root is None:
        return
    
    queue = []
    ret_list = []

    queue.append(g_tree.root)

    while (len(queue) > 0):
        
        root = queue.pop(0)
        ret_list.append(root.value)
        print(root.value)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    return ret_list