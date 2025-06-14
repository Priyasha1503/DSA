
#https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        lst=s.split()
        print(lst)
        return len(lst[-1])
