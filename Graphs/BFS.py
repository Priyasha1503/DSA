
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        vis={0}  ###dding the starting node in to the set...this doesnt create any edge case errors
        bfs=[]
        que=[0] #3adding the starting node
        #print(adj)
        while que:
            node=que.pop(0)
            bfs.append(node)
            for i in adj[node]:#i is neighbour
                if i not in vis:
                    vis.add(i)
                    que.append(i)
                    
        return bfs
            
