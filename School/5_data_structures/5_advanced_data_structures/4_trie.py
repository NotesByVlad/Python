'''
Trie (Prefix Tree)
A Trie is a tree-based data structure used for efficient string operations like prefix matching.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


# Using the Trie class
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

print("Search for 'apple':", trie.search("apple"))  # Output: True
print("Search for 'bat':", trie.search("bat"))      # Output: True
print("Search for 'ball':", trie.search("ball"))    # Output: False
print("Starts with 'app':", trie.starts_with("app"))  # Output: True
