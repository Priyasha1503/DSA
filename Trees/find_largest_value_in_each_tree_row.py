##https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def levelOrder(root):
            if root is None:
                return []
            que=collections.deque()
            que=[root]
            while que:
                size=len(que)
                row=[]
                for i in range(0,size):
                    ele=que.pop(0)
                    row.append(ele.val)
                    if ele.left:
                        que.append(ele.left)
                    if ele.right:
                        que.append(ele.right)
                print(row)
                row.sort(reverse=True)
                res.append(row[0])
            return res
        return levelOrder(root)
            
