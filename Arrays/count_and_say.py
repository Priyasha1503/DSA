
#https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        
        val="1"
        for i in range(1,n+1):
            if i==1:
                val="1"
            else:
                res=""
                i=0
                while i<len(val):
                    cnt=1 #already one ele is ther
                    while i+1<len(val) and val[i]==val[i+1]: #duplicate condn
                        i+=1
                        cnt+=1
                    res+=str(cnt)+val[i]
                    i+=1
                val=res
        return val



A
                
