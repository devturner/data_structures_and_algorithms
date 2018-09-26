from ..linked_list import LinkedList

class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = []

    def __repr__(self):
        pass

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        key = self._hash_key(key)
        self.entries_count += 1
        if key in self.hashtable:
            llist = LinkedList
            llist.append(value)
            self.hashtable[key].append(llist)
        else:
            self.hashtable.append(key, value)

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        key = self._hash_key(key)
        if key in self.hashtable:
            return self.hashtable[key]
        return "Key not in the hash table"

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        key = self._hash_key(key)
        self.entries_count -= 1
        return self.hashtable.pop(key)
