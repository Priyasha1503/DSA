#https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path(root,targetSum,ans,res):
            if root is None:
                return []
            targetSum-=root.val
            ans.append(root.val)
            if root.left is None and root.right is None and targetSum==0:
                res.append(ans[:])
            else:
                path(root.left,targetSum,ans,res)
                path(root.right,targetSum,ans,res)
            ans.pop()
            return res
        return path(root,targetSum,[],[])
    
