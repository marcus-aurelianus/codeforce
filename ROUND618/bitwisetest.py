from itertools import permutations 
a=[ 50 ,55, 60 ,10 ,55]
perm=permutations(a)
def function(lst):
    res=(lst[0]|lst[1])-lst[1]
    for i in range(len(lst)-2):
        res=(res|lst[i+2])-lst[i+2]
    return res
def functionwprint(lst):
    res=(lst[0]|lst[1])-lst[1]
    for i in range(len(lst)-2):
        print(res)
        res=(res|lst[i+2])-lst[i+2]
    return res
out=0
desireperm=[]
for i in list(perm):
    if function(i)>out:
        out=function(i)
        desireperm=[i]
    elif function(i)==out:
        desireperm+=[i]
    


print(out,desireperm)
##for x in range(50,70):
##    for y in range(50,70):
##        if (x|y)-y>(y|x)-x:
##            print(x,y,(x|y)-y,(y|x)-x,y>x)
print(functionwprint([50,10,60,55]))
    
