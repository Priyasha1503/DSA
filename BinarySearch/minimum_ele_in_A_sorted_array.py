
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mins=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid] and nums[mid]<=nums[high]:
                mins=min(mins,nums[low])
                return mins
            if nums[low]<=nums[mid]:#left sorted array
                mins=min(mins,nums[low])
                low=mid+1
            else:
                #right sorted array
                mins=min(mins,nums[mid])
                high=mid-1
        return mins
            
