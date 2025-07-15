
#https://leetcode.com/problems/range-sum-of-bst/?envType=problem-list-v2&envId=nhizork2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ###BRUTEFORCE
        '''def helper(root):
            if root is None:
                return 0
            elif low<=root.val<=high:
                l=helper(root.left)
                r=helper(root.right)
                return l+r+root.val
            else:
                l=helper(root.left)
                r=helper(root.right)
                return l+r+0
        return helper(root)'''
        ###OPTIMAL APPRAOCH
        def helper(root):
            if root is None:
                return 0
            elif root.val<low:
                return helper(root.right)
            elif root.val>high:
               return helper(root.left) 

            #elif root.val<low or root.val>high:  #still not optimised like this
                #return helper(root.left)+helper(root.right)+0
            else:
                return helper(root.left)+helper(root.right)+root.val
        return helper(root) 

