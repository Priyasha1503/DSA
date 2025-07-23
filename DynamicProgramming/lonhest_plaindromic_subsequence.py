#https://leetcode.com/problems/longest-palindromic-subsequence/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''def helper(s,t,x,y):
            if x<0 or y<0 :
                return 0
            elif s[x]==t[y]:
                return 1+helper(s,t,x-1,y-1)
            else:
                c=helper(s,t,x,y-1)
                d=helper(s,t,x-1,y)
                return max(c,d)
        return helper(s,s[::-1],len(s)-1,len(s)-1)'''
        ###MEMOIZATION
        dp=[[-1 for x in range(len(s))]for x in range(len(s))]
        def helper(s,t,x,y):
            if x<0 or y<0:
                return 0
            elif dp[x][y]!=-1:
                return dp[x][y]
            elif s[x]==t[y]:
                dp[x][y]=1+helper(s,t,x-1,y-1)
                return dp[x][y]
            else:
                dp[x][y]=max(helper(s,t,x-1,y),helper(s,t,x,y-1))
                return dp[x][y]
        return helper(s,s[::-1],len(s)-1,len(s)-1)
