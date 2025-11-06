
#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
                #if the left part of the array with respect to low,mid,high is sorted
            if nums[low]<=nums[mid]:
                if nums[low]<=target and target <=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else: #right part of the array is sorted
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
