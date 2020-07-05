import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#3222211133

        
def gift():
    for _ in range(t):
        string = list(input())
        dic={'1':0,'2':0,'3':0}
        s,e=0,0
        n=len(string)
        minlen=0
        while e<n:
            #print(s,e)
            ele=string[e]
            dic[ele]+=1
            if dic['1'] and dic['2'] and dic['3']:
                curmin=e-s+1
                if minlen:
                    minlen=min(minlen,curmin)
                else:
                    minlen=curmin
                for i in range(s,e):
                    dido=string[i]
                    dic[dido]-=1
                    if not (dic['1'] and dic['2'] and dic['3']):
                        #print(e,i)
                        minlen=min(minlen,e-i+1)
                        s=i+1
                        break
            e+=1
        yield minlen
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
