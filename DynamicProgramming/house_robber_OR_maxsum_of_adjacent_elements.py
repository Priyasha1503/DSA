#https://leetcode.com/problems/house-robber/?envType=problem-list-v2&envId=dynamic-programming

'''class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ###RECURSION    
        def helper(ind):
            if(ind==0) : return nums[ind]
            if ind<0: return 0
            pick=nums[ind]+helper(ind-2)
            notpick=0+helper(ind-1)
            return max(pick,notpick)
        
        return helper(len(nums)-1)

        ###MEMOIZATION
        dp=[-1]*(len(nums))
        def helper(ind,dp):
            if(ind==0): return nums[0]
            if(ind<0): return 0
            if dp[ind]!=-1:return dp[ind]
            pick=nums[ind]+helper(ind-2,dp)
            notpick=0+helper(ind-1,dp)
            dp[ind]=max(pick,notpick)
            return dp[ind]

        return helper(len(nums)-1,dp)'''

        ###TABULATION

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        dp[0]=nums[0]
        for ind in range(1,len(nums)):
            pick=nums[ind]
            if ind>1:
                pick=pick+dp[ind-2]
            notpick=0+dp[ind-1]
            dp[ind]=max(pick,notpick)
        return dp[len(nums)-1]
            
