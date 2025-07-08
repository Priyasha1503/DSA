
#https://leetcode.com/problems/min-cost-climbing-stairs/

'''class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ###RECURSION
        def helper(ind):
            if ind==0 or ind==1:
                return 0
            left=helper(ind-1)+cost[ind-1]
            right=helper(ind-2)+cost[ind-2]
            return min(left,right)
        return helper(len(cost))

        ###MEMOIZATION
        dp=[-1]*(len(cost)+1)
        def helper(ind,dp):
            if ind==0 or ind==1:
                return 0
            elif dp[ind]!=-1:
                return dp[ind]
            left=helper(ind-1,dp)+cost[ind-1]
            right=helper(ind-2,dp)+cost[ind-2]
            dp[ind]=min(left,right)
            return dp[ind]
        return helper(len(cost),dp)'''

        ###TABULATION
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*(len(cost)+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)]

