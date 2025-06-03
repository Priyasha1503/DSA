#https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal maxi
            if root is None:
                return 0
            l=helper(root.left)
            r=helper(root.right)
            maxi=max(maxi,l+r)
            return max(l,r)+1
        maxi=0
        helper(root)
        return maxi


'''We return max(left, right) + 1 to the parent → which is height

But we update self.diameter = max(self.diameter, left + right) because that’s a candidate for the longest path

This way, as the recursion climbs up the tree, every possible path is considered — no node is skipped — and the maximum path length is globally tracked in self.diameter.'''
