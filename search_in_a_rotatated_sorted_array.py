#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            #left side is sorted
            if nums[low]<=nums[mid]:
                #check  where the target is...
                if nums[low]<=target and target <=nums[mid]:#if target is present btw low and mid ie left side
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:#if target is present btw mid to high ie right side
                    low=mid+1
                else:
                    high=mid-1
        return -1

                    
