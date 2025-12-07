
#https://leetcode.com/problems/sqrtx/editorial/?source=submission-ac
class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if mid*mid<=x: # it is there in that tick region,so eliminating left
                ans=mid
                low=mid+1
            else:
                high=mid-1
        
        return ans
