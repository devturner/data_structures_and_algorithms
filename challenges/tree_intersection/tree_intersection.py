from .hash_table import HashTable


def tree_intersection(tree1, tree2):
    """ compaire to binary trees and return the values that are common to both of them
    traverse and add all the values of the first tree to a hashtable
    then check if the values from the second are in the hashtable, if so, add them to the return list
    """
    list1 = breadth_first_traversal(tree1)
    list2 = breadth_first_traversal(tree2)
    intersections = []
    ht = HashTable()
    for i in list1:
        ht.set(i, i)

    for i in list2:
        key = ht._hash_key(i)
        if key in ht:
            intersections.append(i)

    return intersections


def breadth_first_traversal(g_tree):
    """ Traverse a binary tree
    """
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
