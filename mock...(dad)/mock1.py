###eliminating the repated words
nums=input().split(",")
lst=nums
res=[]
for i in lst:
    x=i
    i=list(i)
    i.sort()
    flag=0
    for j in range(0,len(i)-1):
        if i[j]==i[j+1]:
            flag=1
    if flag==0:
        
        res.append(nums[lst.index(x)])
        
print(res)



    
