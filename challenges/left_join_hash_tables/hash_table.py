class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [None] * self.table_size

    def __repr__(self):
        return 'Hashtable:' + self.entries_count

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
        hash_key = self._hash_key(key)
        key_val = [key, value]
        if self.hashtable[hash_key] is None:
            self.hashtable[hash_key] = [key_val]
            self.entries_count += 1
        else:
            for item in self.hashtable[hash_key]:
                if item[0] == key:
                    item.append(value)
                    return "Added the value"
            self.hashtable[hash_key].append(key_val)

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the values stored with the key
        """
        hash_key = self._hash_key(key)
        if self.hashtable[hash_key]:
            return self.hashtable[hash_key]
        return "Key not found"

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the values stored with the key
        """
        hash_key = self._hash_key(key)

        if self.hashtable[hash_key] is None:
            return('Key not found')
        for i in range(0, len(self.hashtable[hash_key])):
            if self.hashtable[hash_key][i][0] == key:
                self.entries_count -= 1
                return self.hashtable[hash_key].pop(i)
