from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
def breadth_first_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end = ' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

breadth_first_traversal(root)


