#https://leetcode.com/problems/subarray-sum-equals-k/?envType=problem-list-v2&envId=prefix-sum

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in range(0,len(nums)):
            sums=0

            for j in range(i,len(nums)):
                sums+=nums[j]
                if sums==k:
                    cnt=cnt+1
            
        return cnt

                
