# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if root is None:
                return 0
            sums=0
            if root and root.left and root.left.left is None and root.left.right is None:#root there#root.left there#root.left.left not ther
                sums=sums+(root.left.val)

            l=helper(root.left)
            r=helper(root.right)
            sums=sums+(l+r)
            return sums
        return helper(root)
