# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

##“I’m at a leaf node. Is the remaining targetSum exactly equal to this node’s value?”

        def helper(root,targetSum):
            if root is None:
                return False
            targetSum-=root.val
            if root.left is None and root.right is None  and targetSum==0:
                return True
            #targetSum-=root.val
            return helper(root.left,targetSum) or helper(root.right,targetSum)
        return helper(root,targetSum)
