
#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from math import ceil
class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''min_div=float('inf')
        for x in range(1,max(nums)+1):
            sums=0
            for i in range(0,len(nums)):
                sums+=(ceil(nums[i]/x))
            if sums<=threshold:
                return x'''
        #optimal using Binary search
        def func(mid):
            sums=0
            for i in range(0,len(nums)):
                sums+=(ceil(nums[i]/mid))
            if sums<=threshold:
                return True
        low=1
        high=max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if func(mid): #possible in that region.....
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

