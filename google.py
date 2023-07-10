a = [3,5,4,2]
max_a=max(a)
operation=0
stack=[]
for i in range(len(a)):
    if((max_a-a[i])%2==0):
        operation+=(max_a-a[i])//2
    else:
        if(len(stack)==0):
            stack.append(a[i])
        else:
            e1=stack.pop()
            operation+=1
            operation+=(max_a-a[i]-1)//2
            operation+=(max_a-e1-1)//2
if len(stack)!=0:
    print(-1) 
else:
    print(operation)           