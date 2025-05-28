class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def traversal(root):
    if root:
        print(root.val, end=' ')
        traversal(root.left)
        traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.left = Node(4)
root.left.right.right = Node(3)
root.right.left.left = Node(9)
root.right.left.right = Node(10)
root.right.right.left = Node(13)
root.right.right.right = Node(15)

traversal(root)