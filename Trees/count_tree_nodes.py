#https://leetcode.com/problems/count-complete-tree-nodes/?envType=problem-list-v2&envId=binary-searchcount_tree_node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def count(root):
            if root is None:
                return 0
            else:
                return 1+count(root.left) +count(root.right)
        return count(root)
