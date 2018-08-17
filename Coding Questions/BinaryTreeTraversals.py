
def inorderTraversal(root):
    if root == None:
        return []
    else:
        return inorderTraversal(root.left) + [root] + inorderTraversal(root.right)

def preorderTraversal(root):
    if root == None:
        return []
    else:
        return [root] + preorderTraversal(root.left) + preorderTraversal(root.right)

def postorderTraversal(root):
    if root == None:
        return []
    else:
        return postorderTraversal(root.left) + postorderTraversal(root.right) + [root]

def levelorderTraversal(root):

