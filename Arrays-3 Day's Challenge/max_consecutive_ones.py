#https://leetcode.com/problems/max-consecutive-ones/submissions/1714667612/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        cnt=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                cnt+=1
                max_count=max(max_count,cnt)
            else:
                cnt=0
        return max_count
        
