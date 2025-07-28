
#https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

#User function Template for python3

class Solution:
    def rotate(self, arr):
        '''#bruteforce appraoch - but dont work becuase we have to
        #modify the arr inplace
        temp=[0]*len(arr)
        temp[0]=arr[len(arr)-1]
        print(temp)
        for i in range(0,len(arr)-1):
            temp[i+1]=arr[i]
        return temp'''
        #Optimal approach
        
        temp=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
            
        
    
