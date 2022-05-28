#icopythebinarytree'sjomatech
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


root = Node(12)
root.left = Node(6)
root.right = Node(4)

inorder(root)
