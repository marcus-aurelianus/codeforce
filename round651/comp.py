import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        odd=[]
        even=[]
        for i in range(n*2):
            ele=arry[i]
            if ele%2:
                odd.append(i)
            else:
                even.append(i)
        ans=[]
        if odd:
            leno=len(odd)
            lene=len(even)
            if leno%2:
                for i in range((leno-1)//2):
                    ans.append([odd[2*i],odd[2*i+1]])
                for i in range((lene-1)//2):
                    ans.append([even[2*i],even[2*i+1]])
            else:
                for i in range((leno-2)//2):
                    ans.append([odd[2*i],odd[2*i+1]])
                for i in range((lene)//2):
                    ans.append([even[2*i],even[2*i+1]])
        else:
            m=len(even)
            for i in range((m-2)//2):
                ans.append([2*i,2*i+1])
        for kap in ans:
            yield str(kap[0]+1)+" "+str(kap[1]+1)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
