
#https://leetcode.com/problems/arranging-coins/?envType=problem-list-v2&envId=binary-search

class Solution:
    def arrangeCoins(self, n: int) -> int:
        #Bruteforce
        sums=0
        x=1
        while sums<=n:
            sums+=x
            x+=1
        return x-2 
            
