from typing import Optional, List
from binary_tree_helper import TreeNode, printBinaryTree

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root    
    

preord = [1,2,4,8,9,10,11,5,3,6,7]
inord = [8,4,10,9,11,2,5,1,6,3,7]
sol = Solution()
tree = sol.buildTree(preord, inord)
printBinaryTree(tree)