
#https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        vis=set()
        def bfs(r,c):
            cnt=1#counting for the exisiting pair
            que=collections.deque()
            que.append((r,c))
            vis.add((r,c))
            while que:
                delrow,delcol=que.popleft()
                directions=[[-1,0],[0,-1],[1,0],[0,1]]
                for dr,dc in directions:
                    nrow=dr+delrow
                    ncol=dc+delcol
                    if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and grid[nrow][ncol]==1 and (nrow,ncol) not in vis:
                        que.append((nrow,ncol))
                        vis.add((nrow,ncol))
                        cnt=cnt+1
            return cnt

        maxs=0           
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in vis:
                    x=bfs(r,c)
                    print(x)
                    maxs=max(x,maxs)
        return maxs

            ##O(m × n) — Every cell is visited at most once
