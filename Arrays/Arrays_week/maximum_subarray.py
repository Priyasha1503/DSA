#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ###BRUTEFORCE IN PYTHON WAY
        '''max_sum=-float('inf')
        for i in range(0,len(nums)):
            sums=0
            for j in range(i,len(nums)):
                sums=sums+nums[j]
                max_sum=max(max_sum,sums)
        return max_sum'''
        ###BETTER APPRAOCH - STILL TLE ERROR...
        '''i,j=0,0
        sums=0
        max_sum=-float('inf')
        while i<=len(nums)-1:
            if j==len(nums):              
                i=i+1
                j=i
                sums=0
            else:
                sums=sums+nums[j]
                max_sum=max(max_sum,sums)
                j=j+1
        return max_sum'''
        ###KADANES ALGORITHM
        '''maxending=-float('inf')
        maximum=-float('inf')#result
        for i in range(0,len(nums)):
            maxending=max(maxending+nums[i],nums[i])
            maximum=max(maximum,maxending)
            #max_subarray=      
        return maximum
        #if we have to print the maximum value's subarray'''
        A##REVISION
        max_sum,curr_sum=-float('inf'),0
        maximum=-float('inf')
        for i in range(0,len(nums)):
            maximum=max(maximum+nums[i],nums[i])
            max_sum=max(max_sum,maximum)
        return max_sum
        

        
        


