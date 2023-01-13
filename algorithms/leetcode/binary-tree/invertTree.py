from binary_tree_helper import createBinaryTree, printBinaryTree
class Solution:
    def invertTree(self, root):
        if not root:
            return
        self.invert(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
    
    def invert(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left

tree =  createBinaryTree([4,2,7,1,3,6,9])
sol=Solution()
sol.invertTree(tree)
printBinaryTree(tree)