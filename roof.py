##You are given a pointer to the root of a binary search tree and values to be inserted into the tree.
# Insert the values into their appropriate position in the binary search tree
# and return the root of the updated binary tree. You just have to complete the function.


##A binary search tree is a rooted binary tree data structure with internal nodes that
# each store a key less than all the keys in its right subtree and greater than all the keys in the node’s left subtree.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key <root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.val, end= ' ')
        inorder_traverse(root.right)

root = TreeNode(10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 12)
insert(root, 18)

inorder_traverse(root)






