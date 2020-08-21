import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
nn = "0123456789"

def gift():
    for _ in range(t):
        arry=input()
        n=len(arry)
        dic={}
        dic1={}
        dic2={}
        for i in range(n):
            if i<n-1 and i%2==0:
                freq2=dic2.get(arry[i:i+2],0)
                dic2[arry[i:i+2]]=freq2+1
            elif i<n-1 and i%2:
                freq1=dic1.get(arry[i:i+2],0)
                dic1[arry[i:i+2]]=freq1+1
            freq=dic.get(arry[i],0)
            dic[arry[i]]=freq+1
        #print(dic2)
        yield min(n-dic[max(dic, key=dic.get)],
                  n-(dic2[max(dic2, key=dic2.get)])*2,
                  n-(dic1[max(dic1, key=dic1.get)])*2)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
             


#"{} {} {}".format(maxele,minele,minele)
