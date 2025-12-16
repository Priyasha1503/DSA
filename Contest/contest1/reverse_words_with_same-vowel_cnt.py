
#https://leetcode.com/contest/weekly-contest-480/problems/reverse-words-with-same-vowel-count/

class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(strs):
            '''x=0
            y=len(strs)-1
            while x<y:
                strs[x],strs[y]=strs[y],strs[x]
            return strs'''
            return strs[::-1]

        def count_vowels(strs):
            cnt=0
            for i in strs:
                if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                    cnt+=1
            return cnt

        s=s.split()
        res=[]
        for i in range(0,len(s)):
            if i==0:
                res.append(s[i])
                x=count_vowels(s[i])
            else:
                var=count_vowels(s[i])
                if var==x:
                    res.append(rev(s[i]))
                else :
                    res.append(s[i])
       # print(res)
#print(" ".join(res))
        return " ".join(res)©leetcode
