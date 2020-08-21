n=int(input())

ori=list(input())

steps=list(map(int,input().split()))

tstep=steps[0]

for i in range(1,tstep+1):
    curr=steps[i]
    temp=[]
    for j in range(curr):
        
        if ori[j]=='1':
            temp.append('0')
        else:
            temp.append('1')
    for j in range(curr):
        ori[j],ori[curr-j-1]=temp[curr-j-1],temp[j]
    print(ori)
        

