
#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1822602926/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                #shrinking the array
                low+=1
                high-=1
                continue
            elif nums[low]<=nums[mid]: #if the left aprt of the mid is sorted
                if nums[low]<=target and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else: #else the right part is sorted
                if nums[mid]<=target and nums[target]<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
