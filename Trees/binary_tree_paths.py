
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


 '''1. Why res.append(ans[:]) instead of res.append(ans)?
When using backtracking, the list ans keeps changing as recursion unfolds. If you append ans directly, you're adding a reference — so future changes to ans will reflect in res. Using ans[:] creates a shallow copy (a snapshot) of the current state. This ensures that previously added paths in res stay unchanged, even as ans backtracks.

 2. Why not use res as a global variable?
Using a global res can lead to bugs, especially when functions are called multiple times (e.g., during test cases). Globals retain old values unless manually cleared, making results unpredictable. It also breaks encapsulation — the function becomes harder to debug, test, and reuse. Keeping res local (as a parameter or return value) ensures clean, controlled recursion.

'''
            
