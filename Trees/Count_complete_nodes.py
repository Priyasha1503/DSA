# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #we could do generally any traversal and then while dng it ,we could count down the nodes
        #and I am gng with preordeer here...thought to actually go with level order..but I dont get it much...
        def helper(root,cnt):
            if root is None:
                return cnt

            else:
                #PREORDER - PARENT - LEFT - RIGHT
                print("cnt is",cnt)
                x=helper(root.left,cnt)
                y=helper(root.right,cnt)
                #cnt=cnt+(x+y)
                #no need of count var, no need of it in func parameters too
                return x+y+1
        return helper(root,0)
        return cnt
            

