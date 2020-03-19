import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        dic={}
        ans=False
        for i in range(n):
            ina=dic.get(lst[i],[])
            #print(dic,ina,i-1)
            if ina and i!=0:
                #print(i-1 in ina,i-1,ina)
            
                if i-1 not in ina or len(ina)>=2:
                    ans=True
                    break

                    
            ina.append(i)
            dic[lst[i]]=ina
        if ans:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

