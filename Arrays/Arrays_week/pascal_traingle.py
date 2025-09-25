#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(0,numRows):
            if i==0:
                res.append([1])
            elif i==1:
                res.append([1,1])
            else:
                print(res[-1])
                arr=res[-1]
                lst=[1]
                for i in range(0,len(arr)-1):
                    lst.append(arr[i]+arr[i+1])
                lst.append(1)
                res.append(lst)
        return res



