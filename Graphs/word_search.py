##https://leetcode.com/problems/word-search/?envType=problem-list-v2&envId=depth-first-search

### RECURSION (DFS) WITH BACK TRACKING  IS OPTIMAL , RATHER THAN MEMOIZATION AND TABULATION - FOR MEMOIZATION USING HASHMAP IS MORE EFFECTIVE RTHER THAN THE BELOW METHOD DONE... because chatgpt said this is the things"Correctly captures (r, c, index) or even visited: when we use the dict 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows=len(board)
        cols=len(board[0])
        vis=set()
        def dfs(ind,r,c):
            if ind==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            if (r,c) in vis:
                return False
            if board[r][c]!=word[ind]:
                return False
            vis.add((r,c))
            dir1=dfs(ind+1,r+1,c)
            dir2=dfs(ind+1,r,c+1)
            dir3=dfs(ind+1,r-1,c)
            dir4=dfs(ind+1,r,c-1)
            vis.remove((r,c))
            return dir1 or dir2 or dir3 or dir4

        for r in range(0,rows):
            for c in range(0,cols):
                if board[r][c]==word[0]:
                    if (r,c) not in vis:
                        if dfs(0,r,c):
                            return True
        return False 
##MEMIOZATION
'''class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows=len(board)
        cols=len(board[0])
        vis=set()
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(ind,r,c):
            if ind==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            if (r,c) in vis:
                return False
            if board[r][c]!=word[ind]:
                return False
            if dp[r][c]!=-1:
                return dp[r][c]
            vis.add((r,c))
            dir1=dfs(ind+1,r+1,c)
            dir2=dfs(ind+1,r,c+1)
            dir3=dfs(ind+1,r-1,c)
            dir4=dfs(ind+1,r,c-1)
            vis.remove((r,c))  ##backtrack
            dp[r][c]=dir1 or dir2 or dir3 or dir4
            return dp[r][c]

        for r in range(0,rows):
            for c in range(0,cols):
                if board[r][c]==word[0]:
                    if (r,c) not in vis:
                        if dfs(0,r,c):
                            return True
        return False'''
