class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sets=set()
        maxcnt=0
        cnt=0
        for  i in range(0,len(nums)):
            if nums[i]==0:
                maxcnt=max(cnt,maxcnt)
                cnt=0
            else:
                cnt=cnt+1
        maxcnt=max(maxcnt,cnt)
        return maxcnt




            
