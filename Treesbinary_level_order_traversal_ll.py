
#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ##levelorder tarversal
        if root is None:
            return []
        res=[]
        que=[root]
        while que:
            row=[]
            for _ in range(0,len(que)):
                node=que.pop(0) #element is (removed) and stored
                row.append(node.val)
                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            res.append(row)
        return res[::-1]
