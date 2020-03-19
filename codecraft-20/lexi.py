import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def lexi(a,b):
    lenof=len(a)
    for i in range(lenof):
        #print(a[i],b[i])
        if a[i]==b[i]:
            continue
        elif a[i]<b[i]:
            return True
        else:
            return False
    return False
def gift():
    for _ in range(t):
        n=int(input())
        string=input()
        loweststring=string[0]
        lowestpos=[0]
        for i in range(1,n):
            #print(string[i])
            if ord(string[i])<ord(loweststring):
                loweststring=string[i]
                lowestpos=[i]
            elif string[i]==loweststring:
                lowestpos.append(i)
        correstring=[]
        #print(lowestpos)
        nonrepeat=[]
        for i in lowestpos:
            if i%2==(n-1)%2:
                tempstring=string[i:]+string[:i][::-1]
            else:
                tempstring=string[i:]+string[:i]
   
            #print(correstring)
            if tempstring not in nonrepeat:
                nonrepeat.append(tempstring)
                correstring.append([tempstring,i+1])

        ans,ansinde=correstring[0]
        
        lenans=len(correstring)

        
        for i in range(lenans-1):
             if lexi(correstring[i+1][0],ans):
                 ans,ansinde=correstring[i+1]
        
        yield ans
        yield ansinde
#print(lexi('abba','abab'))      
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
