
#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #base cond
        #if root.left,append val
        #if root.right,append val
        #again should store nodes of one level in one lst,and hsould append them to the res list
        if  root is None:
            return []
        que=[root]
        res=[]
        while que:
            l=len(que)
            curr_level=[]
            for _ in range(l):
                node=que.pop(0)
                curr_level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(curr_level)
            
        return res
