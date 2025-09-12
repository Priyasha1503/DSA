###PRINT THE HIGHEST PRODUCT'S BITH NUMBERS
#eg:if x*y is the highest product,print(x,y)
nums=list(map(int,input().split()))
max_prod=0
res=[]
for i in range(0,len(nums)-1):
    if nums[i]*nums[i+1]>max_prod:
        
        max_prod=nums[i]*nums[i+1]
        res=[nums[i],nums[i+1]]
print(res)
    
    
