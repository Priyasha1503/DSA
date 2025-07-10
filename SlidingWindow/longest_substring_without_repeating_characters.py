
##https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #BRUTEFORCE -O(n2)
        '''maxs=0
        for i in range(0,len(s)):
            vis=set()
            j=i
            cnt=0
            while j<len(s) and s[j] not in vis :
                vis.add(s[j])
                cnt=cnt+1
                j=j+1

            maxs=max(cnt,maxs)
        return maxs'''
        #better appraoch o(n)
        if s=="":
            return 0
        if len(s)==1:
            return 1
        maxs=0
        start=0
        end=1
        vis=set(s[0])
        while end<len(s):
            if s[end] not in vis:
                vis.add(s[end])
                end=end+1
                maxs=max(maxs,end-start)
            else:
                vis.remove(s[start])
                start+=1
                
        return maxs   






