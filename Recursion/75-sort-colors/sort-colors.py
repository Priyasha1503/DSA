class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt1,cnt2,cnt3=0,0,0
        c1,c2,c3=0,0,0
        for i in range(0,len(nums)):
            if nums[i]==0:
                cnt1=cnt1+1  #cnt for zeroes
            elif nums[i]==1:
                cnt2=cnt2+1   #cnt for ones
            else:
                cnt3=cnt3+1   #cnt for twos
        for x in range(0,cnt1):
            nums[x]=0
        for x in range(cnt1,cnt2+cnt1):
            nums[x]=1
        for x in range(cnt2+cnt1,len(nums)):            #cnt+cnt2+cnt3 can be written or len(nums) can be wrriten 
            nums[x]=2
        return nums

