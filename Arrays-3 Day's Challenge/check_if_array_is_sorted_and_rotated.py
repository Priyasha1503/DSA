#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        #BRUTEFORCE IN PYTHON
        for i in range(0,len(nums)):
            lst=nums[i:]+nums[:i]
            flag=True
            for i in range(0,len(lst)-1):
                if lst[i]>lst[i+1]:
                    flag=False
                    break
            if flag:
                return True
        return False

                
