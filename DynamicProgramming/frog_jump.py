
#https://www.geeksforgeeks.org/problems/geek-jump/1

#User function Template for python3
'''class Solution:
    def minCost(self, height):
        # code here
        ###RECURSION
        def helper(ind):
            if ind==0:
                return 0
            left=helper(ind-1)+abs(height[ind]-height[ind-1])
            right=helper(ind-2)+abs(height[ind]-height[ind-2])
            return min(left,right)
        return helper(len(height)-1)
        
        
        ###MEMOIZATION
        dp=[-1]*(len(height))
        def helper(ind,dp):
            if ind==0: 
                return 0
            elif dp[ind]!=-1: 
                return dp[ind]
            
            l=helper(ind-1,dp)+abs(height[ind]-height[ind-1])
            if ind>1 : 
                r=helper(ind-2,dp)+abs(height[ind]-height[ind-2])
            else:
                r=float('inf')
            dp[ind]=min(l,r)
            return dp[ind]
        return helper(len(height)-1,dp)
        
        '''
class Solution:
    def minCost(self, height):
        
        ###TABULATION
        dp=[0]*(len(height))
        dp[0]=0
        for ind in range(1,len(height)):
            l=dp[ind-1]+abs(height[ind]-height[ind-1])
            r=float('inf')
            if ind>1:
                r=dp[ind-2]+abs(height[ind]-height[ind-2])
            dp[ind]=min(l,r)
        return dp[len(height)-1]
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
