
#https://leetcode.com/problems/height-checker/?envType=problem-list-v2&envId=array

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=[]
        for i in heights:
            expected.append(i)
        expected.sort()
        print(heights)
        print(expected)
        cnt=0
        for i in range(0,len(heights)):
            if heights[i]!=expected[i]:
                cnt=cnt+1
        return cnt
