#https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxs=0
        cnt=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                cnt=cnt+1
                maxs=max(cnt,maxs)
            else:
                print(cnt)
                #maxs=max(cnt,maxs) max is checked while nums[i]=1 not in the else part
                cnt=0

        return maxs
