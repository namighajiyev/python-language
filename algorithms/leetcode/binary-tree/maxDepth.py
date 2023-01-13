
from binary_tree_helper import createBinaryTree, printBinaryTree

class Solution:
    def maxDepth(self, root):
        return 1   
    
    def maxDepthHelper(self, root, level) :
        if not root:
            return 0
       # left = maxDepthHelper(root.left, level)
        
# [3,9,20,null,null,15,7]
tree =  createBinaryTree([3,9,20,None,None,15,7])
sol=Solution()
maxDepth = sol.maxDepth(tree)
printBinaryTree(tree)
print(maxDepth)