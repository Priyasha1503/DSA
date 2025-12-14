
#https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lst=[]
        def dfs(root):
            if root is None:
                return
            lst.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return lst
        
        lst=dfs(root)
        c=Counter(lst)
        maxs=-1
        res=[]
        for i in c:
            if c[i]>maxs:
                maxs=c[i]
        for i in c:
            if c[i]==maxs:
                res.append(i)
        return res
        
        
