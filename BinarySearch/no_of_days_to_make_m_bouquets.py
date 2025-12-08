
#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        '''map=dict()

        for i in range(0,len(bloomDay)):
            if bloomDay[i] not in map:
                map[bloomDay[i]]=set()
                map[bloomDay[i]].add(i)           ####SOME APPROACH IM TRYING USING HASHMAP INSTEAD OF BINSEARCH

            else:
                map[bloomDay[i]].add(i)
        print(map)

        for i in map:'''
        def func(mid):
            cnt=0
            no_of_bokeys=0
            for i in range(0,len(bloomDay)):
                if bloomDay[i]<=mid:
                    cnt+=1
                else:
                    no_of_bokeys+=(cnt//k)
                    cnt=0
            no_of_bokeys+=(cnt//k)
            if no_of_bokeys>=m:
                return True
            else:
                return False

        ans=-1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            res=func(mid)
            if res: #possible region......eleimiating righ side
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans


             





             
             


