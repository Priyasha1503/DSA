#https://leetcode.com/problems/majority-element/submissions/1783453211/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #BRUTEFORCE - Taking a counter from collections,so that I could know the frequency, and compare the frequencies  -- but this couldnt be solved in o(1) space comp
        ###BOYER MOORE ALGORITHM
        candidate=None
        count=0
        for i in nums:
            if count==0:
                candidate=i
            if candidate==i:
                count+=1
            else:
                count-=1
        return candidate
        
