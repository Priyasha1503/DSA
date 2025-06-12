#https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ##appraoch - If there are -1s in the direction..then not ount the whole bfs..

        rows,cols=len(grid),len(grid[0])
        vis=set()
        def bfs(r,c):
            bound=0#boundary
            if r==0 or r==rows-1 or c==0 or c==cols-1:##to check boundary condn for the inserted pair in the que
                bound=1
            cnt=1##1 is taken since we count the existing pair
            que=collections.deque()
            que.append((r,c))
            vis.add((r,c))
            while que:
                delrow,delcol=que.popleft()
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    nrow=dr+delrow
                    ncol=dc+delcol
                    '''if nrow==0 or nrow==rows-1 or ncol==0 or ncol==cols-1:
                        bound=1'''
    
                    if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and grid[nrow][ncol]==1 and (nrow,ncol) not in vis:
                        if nrow==0 or nrow==rows-1 or ncol==0 or ncol==cols-1:##boundary condn
                            bound=1

                        que.append((nrow,ncol))
                        vis.add((nrow,ncol))
                        cnt=cnt+1

                    '''if bound==1:
                        pass
                    else:
                        cnt=cnt+1'''
            return (cnt,bound)
                             
        total_count=0
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c]==1 and (r,c) not in vis:
                    x,b=bfs(r,c)
                    if b==1:
                        pass
                    else:

                        total_count=total_count+x
        return total_count

