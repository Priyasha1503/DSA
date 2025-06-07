
#https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def path(root,ans,res):
            if root is None:
                return 0
            root.val=str(root.val)
            ans.append(root.val)
            if root.left is None and root.right is None:#leaf condn
                lst=ans[:]
                j="".join(lst)
                res.append(j)
            else:
                path(root.left,ans,res)
                path(root.right,ans,res)
            ans.pop()
            return res
        res=[]
        path(root,[],res)
        sums=0
        for i in res:
            sums=sums+int(i)
        return sums



            
