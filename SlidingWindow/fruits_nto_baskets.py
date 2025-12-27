
#https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''mpp=dict()
        l,r=0,0
        maxlen=1
        while r<len(fruits):
            mpp[fruits[r]]=mpp.get(fruits[r],0)+1
            while len(mpp)>2:
                mpp[fruits[l]]-=1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen'''
        mpp=dict()
        l,r=0,0
        maxlen=1
        while r<len(fruits):
            mpp[fruits[r]]=mpp.get(fruits[r],0)+1
            if len(mpp)>2:
                mpp[fruits[l]]-=1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
