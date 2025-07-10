#https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #BRUTEFORCE-PYTHON VERSION -TLL
        '''if len(nums)==1 and k==1:
            return float(nums[0])
        maxs=-float('inf')
        for x in range(0,len(nums)-k+!):
            maxs=max(maxs,float(sum(nums[x:x+k]))/k)
        return maxs'''
        #better approach
        if(len(nums)==1 and k==1):
            return float(nums[0])
        first_sum=float(sum(nums[0:k]))
        maxs=float(first_sum/k)
        for i in range(1,len(nums)-k+1):
            first_sum=first_sum-float(nums[i-1])+float(nums[k+i-1])
            maxs=max(maxs,first_sum/k)
        return maxs

