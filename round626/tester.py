n=8
lefstk=[0,4,3,5]
rigstk=[2,1,6,7]
res=""
for i in range(n):
    if i in lefstk:
        res+="("
    else:
        res+=")"
print(res)
