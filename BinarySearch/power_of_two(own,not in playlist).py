
#https://leetcode.com/problems/power-of-two/
#perfect nuber - solved in binary search---dng the  playlist,but this prob wasnt there...this Im solving randomly...and then I got this idea..

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        low=0 
        high=31    ## because 2^31 exceeds 2 billion
        while low<=high:
            mid=(low+high)//2
            res=2**mid
            if res==n:
                return True
            elif res>n:
                high=mid-1
            else:
                low=mid+1
        return False
