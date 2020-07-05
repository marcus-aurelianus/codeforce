import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        
        n,m = list(map(int,input().split()))
        table = input()

        blanks=[]
        counter=0
        onerino=0
        typelst=[]
        typerino='cl'
        revcounter=0
        revtype=[]

        tuperinorev='bl'
        
        for i in range(n):
            if table[i]=='1':
                
                onerino+=1
                if counter:
                    
                    blanks.append(counter)
                    typelst.append(typerino)
                    counter=0
                typerino="cr"
            else:
                counter+=1
                if i==n-1:
                    blanks.append(counter)
                    typelst.append(typerino)
            if table[n-i-1]=='1':

                if revcounter:
                    
 
                    revtype=[tuperinorev]+revtype
                    revcounter=0
                tuperinorev="br"
            else:
                revcounter+=1
                if i==n-1:
                    
                    revtype=[tuperinorev]+revtype
        
        #yield typelst,revtype,blanks
        ans=0
        jibai=len(blanks)
        for i in range(jibai):
            ele=blanks[i]
            if typelst[i]=='cl' and revtype[i]=='bl':
                ans+=1+(ele-1)//(m+1)
            elif typelst[i]=='cl' or revtype[i]=='bl':
                ans+=ele//(m+1)
            else:
                
                ans+=max(0,(ele-m)//(m+1))
                
        yield ans
                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
