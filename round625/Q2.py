import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    t= int(input())
    beauti = list(map(int,input().split()))
    res=0
    dic={}
    newlen=0
    for i in range(t):
        realval=beauti[i]-i


        getit=dic.get(realval,0)
        dic[realval]=getit+beauti[i]
   # print(dic)
        
    
    print(dic[max(dic, key=dic.get)])
            
        

            
