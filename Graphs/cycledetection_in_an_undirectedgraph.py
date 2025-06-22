#https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1


from collections import defaultdict
from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        def bfs(start):
            que=deque()
            que.append((start,-1))##starting node
            vis.add(start)
            while que:
                delnode,delparent=que.popleft()
                for nbr in adj[delnode]:
                    if nbr not in vis:
                        vis.add(nbr)
                        que.append((nbr,delnode))
                    elif nbr in vis and nbr!=delparent:
                        return True
            return False
                        
        for i in range(V):
            if i not in vis:
                if bfs(i):
                    return True
                    
        return False
                

        
        
            
		        
