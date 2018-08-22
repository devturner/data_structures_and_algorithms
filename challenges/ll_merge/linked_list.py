from .node import Node


class LinkedList(object):
    def __init__(self, iterable=None):
        self.head = None
        self._length: int = 0

        if iterable is None:
            iterable = []
        for value in iterable:
            self.insert(value)

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def __iter__(self):
        if self.head:
            self._current = self.head
        return self

    def insert(self, val):
        """
        """

        self.head = Node(val, self.head)
        self._length += 1

        return self.head.val

    def append(self, val):
        self.head = Node(val, self.head)
        current = self.head
        while current._next:
            current = current._next
        new_node = Node(val)
        current._next = new_node
        self._length += 1

    def insert_before(self, v1, v2):
        current = self.head
        while current._next.val != v1:
            current = current._next
        current._next = Node(v2, current._next)
        self._length += 1      
    
    def insert_after(self, v1, v2):
        current = self.head
        while current.val != v1:
            current = current._next
        current._next = Node(v2, current._next)
        self._length += 1

    def includes(self, val):
        """Linked List method which returns the first matching node, else None
        """
        current = self.head

        while current is not None:
            if current.val == val:
                return True
            current = current._next

        return False

    def kth_from_the_end(self, arg):
        var2 = 0
        current = self.head

        while current._next:
            var2 += 1
            current = current._next
        
        front_index = var2 - arg
        current = self.head
        while front_index != 0:
            front_index -= 1
            current = current._next

        return current.val
            