from .linked_list import LinkedList


def ll_merge(linked_list_1, linked_list_2):
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    linked_list_3 = LinkedList()
    linked_list_3.append(cur1.val)
    while (cur1 is not None) and (cur2 is not None):        
        if cur1._next:
            linked_list_3.append(cur1.val)
            cur1 = cur1._next            
        if cur2._next:
            linked_list_3.append(cur2.val)
            cur2 = cur2._next
    
    return linked_list_3
