
#https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        dfs=[0]
        #vis=set(0)
        ##set([1,2,3]) is accepted but nor set(0)..basiaclly itrables are accepted 
        vis=set()
        vis.add(0) # or vis={0}
        
        def depth(node,adj):
            for neighbour in adj[node]:
                if neighbour not in vis: #marking it visited basically
                    vis.add(neighbour)
                    dfs.append(neighbour)
                    depth(neighbour,adj)
            
        depth(0,adj)
        return dfs
            
