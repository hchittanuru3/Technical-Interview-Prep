
def inorderTraversal(root):
    if root == None:
        return []
    else:
        return inorderTraversal(root.left) + [root] + inorderTraversal(root.right)