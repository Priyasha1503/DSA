
#https://leetcode.com/problems/jewels-and-stones/?envType=problem-list-v2&envId=hash-table

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sets=set(jewels)
        cnt=0
        for i in stones:
            if i in sets:
                cnt=cnt+1
        return cnt
            
