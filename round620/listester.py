lst=[7 ,6 ,1, 5, 4, 2 ,3]
n=len(lst)
res=""
for i in range(n-1):
    if lst[i]<lst[i+1]:
        res+="<"
    else:
        res+=">"
print(res)
