'''
Hash Table
A hash table is a data structure that maps keys to values using a hash function for fast lookups.
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Compute a hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        """Search for a value by its key."""
        index = self._hash(key)
        if self.table[index]:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def display(self):
        """Display the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Using the HashTable class
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "New York")

print("Hash Table:")
ht.display()
print("Search for 'name':", ht.search("name"))  # Output: Alice
print("Search for 'age':", ht.search("age"))    # Output: 25
