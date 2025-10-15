
#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


class Solution:
    def check(self, nums: List[int]) -> bool:
        #BRUTEFORCE IN PYTHON
        '''for i in range(0,len(nums)):
            lst=nums[i:]+nums[:i]
            flag=True
            for i in range(0,len(lst)-1):
                if lst[i]>lst[i+1]:
                    flag=False
                    break
            if flag:
                return True
        return False'''
        if len(nums)==1: return True
        cnt=1
        n=len(nums)
        for i in range(1,2*n):
            if nums[(i-1)%n]<=nums[i%n]:
                cnt+=1
            else:
                cnt=1
            if cnt==n:
                return True
        
        return False


                



                
