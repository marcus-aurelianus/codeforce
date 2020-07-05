import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


#print(len(inamo))
def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        dic={}
        for ele in arry:
            freq=dic.get(ele,0)
            dic[ele]=freq+1
        maxbro=max(dic, key=dic.get)
        manum=dic[maxbro]
        other=len(dic)-1
        #print(dic,len(dic))
        if manum>other:

            yield min((manum+other)//2,other+1)
        else:
            yield manum
 
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
