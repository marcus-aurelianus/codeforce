a=[0,3,-2,5,-1]
b=[0]
a.sort()
print(a)
for num in a:
    ele=b[-1]+num
    b.append(ele)
b=b[1:]
print(b)
