#https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

#DFS 
from collections import defaultdict
class Solution:
	def isCycle(self, V, edges):
	    #adjacenmcy list
	    adj=defaultdict(list)
	    vis=set()
	    for u,v in edges:
	       adj[u].append(v)
	       adj[v].append(u)
        #dfs
        def dfs(node,parent,vis,adj):
            vis.add(node)
            for i in adj[node]:
                if i not in vis:
                    if(dfs(i,node,vis,adj)):#if it is true
                        return True
                elif i!=parent:
                    return True
            return False
            
        #continuation of main func
        for x in range(V):
            if x not in vis:
                if dfs(x,-1,vis,adj):
                    return True
        return False
                    
    
	    
        
