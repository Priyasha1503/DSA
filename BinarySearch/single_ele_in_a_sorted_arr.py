
#https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''#one appraoch is two take freq or count of the values or items
        ans=-1
        for i in range(0,len(nums)-1):
            if i%2==0:
                if nums[i]==nums[i+1]:
                    pass
                else:
                    ans=nums[i]
                    break
        if ans!=-1:
            return ans
        else:
            return nums[-1]'''
        #USING BNARY SEARCH
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        
        low,high=1,n-2
        while low<=high:
            mid=(low+high)//2
            #checking kinda mid condition
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
                #checking left condn
            if mid%2==0 and nums[mid]==nums[mid+1]:
                low=mid+1
            elif mid%2==1 and nums[mid]==nums[mid-1]:    #mid%2==1 resembles the condition of odd
                low=mid+1
            else:
                high=mid-1
        return -1 ### this will not be exected to any test case, up only everything will be returned


            


