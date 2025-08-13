
#https://leetcode.com/problems/minimum-path-sum/

'''class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ##BruteForce
        m,n=len(grid),len(grid[0])
        minsum=float('inf')
        def minpath(r,c,grid):
            if r<0 or c<0 or r>=m or c>=n:
                return float('inf')
            if r==m-1 and c==n-1: #reaching the detsination
                return grid[r][c]
            
            else:
                down=grid[r][c]+minpath(r+1,c,grid)
                right=grid[r][c]+minpath(r,c+1,grid)
                minsum=min(down,right)
                return minsum

        return minpath(0,0,grid)
        m,n=len(grid),len(grid[0])
        minsum=float('inf')
        dp=[[-1 for x in range(n)] for _ in range(m)]

        def minpath(r,c,grid):
            if r<0 or c<0 or r>=m or c>=n:
                return float('inf')
            if r==m-1 and c==n-1: #reaching the detsination
                return grid[r][c]
            elif dp[r][c]!=-1:
                return dp[r][c]

            
            else:
                down=grid[r][c]+minpath(r+1,c,grid)
                right=grid[r][c]+minpath(r,c+1,grid)
                minsum=min(down,right)
                dp[r][c]=minsum
                return dp[r][c]

        return minpath(0,0,grid)'''
        
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for r in range(m):
            for c in range(n):
                if
