
#https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #BRUTEFORCE -PYTHON WAY
        '''sum_l=0
        sum_r=0
        for i in range(0,len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1'''

        l_sum=0
        r_sum=sum(nums)
        for i in range(0,len(nums)):
            r_sum-=nums[i]
            if l_sum==r_sum:
                return i
            l_sum+=nums[i]
        return -1
