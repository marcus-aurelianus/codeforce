string='abcdefghi'
n=len(string)
for i in range(1,n+1):
    tempstring=string
    for j in range(n-i+1):
        #print(i,j,j+i+1)
        #print(tempstring[:j],tempstring[j:j+i-1][::-1],tempstring[j+i-1:])
        tempstring=tempstring[:j]+tempstring[j:j+i][::-1]+tempstring[j+i:]
        #print(tempstring)
    print(i-1,tempstring)
