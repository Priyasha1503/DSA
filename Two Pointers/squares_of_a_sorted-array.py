
#https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''res=[]
        for i in nums:
            res.append(i*i)
        res.sort()
        return res'''
        res=[-1]*len(nums)
        left=0
        right=len(nums)-1
        i=len(nums)-1
        while left<=right:
            leftval=nums[left]*nums[left]
            rightval=nums[right]*nums[right]
            if leftval<rightval:
                res[i]=rightval
                right-=1
            else:
                res[i]=leftval
                left+=1
            i-=1

        return res
