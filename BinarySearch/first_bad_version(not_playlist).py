
#https://leetcode.com/problems/first-bad-version/?envType=problem-list-v2&envId=binary-search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        #Bruteforce
        '''for i in range(1,n+1):
            if (isBadVersion(i)):
                return i'''
        
        #Optimal - BinaraySearch
        low=1
        high=n
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low   #we can return here ans or low...low because we are using the conept "Opposite Polarity" from striver
