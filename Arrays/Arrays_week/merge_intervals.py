
#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        start=intervals[0][0]
        end=intervals[0][1]  #start and end are to comparee
        
        for i in range(0,len(intervals)):
            if end>=intervals[i][0]:
                end=max(intervals[i][1],end)
            else:
                res.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        res.append([start,end])
        return res
