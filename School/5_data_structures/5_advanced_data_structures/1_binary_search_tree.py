'''
 Binary Search Tree (BST)
A Binary Search Tree (BST) is a tree where:

Each node has at most two children: left and right.
The left subtree of a node contains only nodes with values less than the node's value.
The right subtree of a node contains only nodes with values greater than the node's value.
'''

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = BSTNode(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = BSTNode(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None or current.key == key:
            return current is not None
        if key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def inorder(self):
        """Perform in-order traversal (Left, Root, Right)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)


# Using the BinarySearchTree class
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order traversal:", bst.inorder())  # Output: [20, 30, 40, 50, 60, 70, 80]
print("Search for 40:", bst.search(40))      # Output: True
print("Search for 90:", bst.search(90))      # Output: False
