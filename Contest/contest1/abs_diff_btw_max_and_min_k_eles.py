
#https://leetcode.com/contest/weekly-contest-480/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        small=sum(nums[0:k])
        large=sum(nums[len(nums)-k:])
        return abs(small-large)©leetcode
