
#https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0
        rows,cols=len(board),len(board[0])
        vis=set()
        def bfs(r,c):
            region=set()
            bound=0
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                bound=1
            que=collections.deque()
            que.append((r,c))
            vis.add((r,c))
            region.add((r,c))
            while que:
                delrow,delcol=que.popleft()
                directions=[[-1,0],[0,-1],[1,0],[0,1]]
                for dr,dc in directions:
                    nrow=dr+delrow
                    ncol=dc+delcol
                    if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and board[nrow][ncol]=='O' and (nrow,ncol) not in vis and (nrow,ncol) not in region:
                        if nrow==0 or nrow==rows-1 or ncol==0 or ncol==cols-1:
                            bound=1

                        que.append((nrow,ncol))
                        vis.add((nrow,ncol))
                        region.add((nrow,ncol))
            return (bound,region)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and (r,c) not in vis:
                    b,reg=bfs(r,c)
                    print(b)
                    print(reg)
                    if b==1:#boundary is touched
                        pass
                    else:
                        for i,j in reg:
                            print("yess")
                            board[i][j]='X'


