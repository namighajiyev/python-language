# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    createBinaryTreeHelper(arr, root, 0)
    return root
        
    
def createBinaryTreeHelper(arr, root, index):
    if index >= len(arr):
        return None
    leftIndx, rightIndx = index * 2 +1, index *2 +2
    if len(arr) > leftIndx:
        root.left =TreeNode(arr[leftIndx])
    if len(arr) > rightIndx:
        root.right =TreeNode(arr[rightIndx])
    createBinaryTreeHelper(arr, root.left, leftIndx)
    createBinaryTreeHelper(arr, root.right, rightIndx) 
    
def printBinaryTree(root):
    arr = [] if not root else [root.val]
    printBinaryTreeHelper(root, arr)
    print(arr)

def printBinaryTreeHelper(root, arr):
    if not root:
        return
    if root.left:
        arr.append(root.left.val)
    if root.right:
        arr.append(root.right.val)
    printBinaryTreeHelper(root.left,arr)
    printBinaryTreeHelper(root.right,arr)
        

# tree = createBinaryTree([4,2,7,1,3,6,9])
# printBinaryTree(tree)

'''
Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
'''