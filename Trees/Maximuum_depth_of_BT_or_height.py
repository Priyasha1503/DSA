# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        print(" l is ",l)
        print("r is ",r)
        return max(l,r)+1        

        #return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
