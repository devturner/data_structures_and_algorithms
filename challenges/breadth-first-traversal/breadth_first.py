from queue import Queue



def breadth_first_traversal(g_tree):
    qt = Queue()
    ret_list = []
    if g_tree.root is None:
        return
    
    qt.enqueue(g_tree.root)

    while qt._length > 0:
        # import pdb; pdb.set_trace()
        if g_tree.root.left:
            qt.enqueue(g_tree.root.left)
        if g_tree.root.right:
            qt.enqueue(g_tree.root.right)
        ret_list.append(qt.dequeue)
    
    return ret_list