from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self._length: int = 0

        # if iterable is None:
        #     iterable = []

        # for value in iterable:
        #     self.insert(value)

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

    def includes(self, val):
        """Linked List method which returns the first matching node, else None
        """
        current = self.head

        while current is not None:
            if current.val == val:
                return True
            current = current._next

        return False


    # def includes(self, val: str, data: int) -> bool:
    # def find(self, val):
        