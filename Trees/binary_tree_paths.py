
#https://leetcode.com/problems/binary-tree-paths/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        

        def path(root,ans,res):
            if root is None:
                return None
            ans.append(root.val)
            if root.left is None and root.right is None :
                lst=ans[:]
                lst=[str(x) for x in ans ]
                j="->".join(lst)
                res.append(j)

            else:   
                path(root.left,ans,res)
                path(root.right,ans,res)
            ans.pop()
            return res
        return path(root,[],[])

            
