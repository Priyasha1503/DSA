#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        x=self.helper(root,[])
        return x
        
    #ROOT - LEFT - RIGHT

    def helper(self,root,lst):
        if root is None:
            return lst
        else:
            lst.append(root.val)
            
            self.helper(root.left,lst)
            self.helper(root.right,lst)
        return lst
