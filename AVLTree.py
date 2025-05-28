class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, m):
        y = m.right
        T2 = y.left
        y.left = m
        m.right = T2
        m.height = 1 + max(self.get_height(m.left), self.get_height(m.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, m):
        y = m.left
        T3 = y.right
        y.right = m
        m.left = T3
        m.height = 1 + max(self.get_height(m.left), self.get_height(m.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance (self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

avl_tree = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl_tree.insert(root, key)
def pre_order(node):
    if not node:
        return
    print(f"{node.key}", end=" ")
    pre_order(node.left)
    pre_order(node.right)

pre_order(root)

