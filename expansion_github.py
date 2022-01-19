def fun_expand(I):
    l=[]
    flag=0
    for j in range(0,len(I)-1):
        diff=abs(I[j+1]-I[j])
        l.append(diff)
    for i in range(0,len(l)-1):
        if l[i]>=l[i+1]:
            flag=1
    if flag==1:
        return "false"
    else:
        return "true"
            
I=list(map(int,input().split()))
x=fun_expand(I)
print(x)