import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def erase():
    for _ in range(t):
        string=input()
        find=False
        count1,count2=0,0
        for ele in string:
            if not find:
                if ele=='1':
                    find=True
            else:
                if ele=='0':
                    count1+=1
                else:
                    count2=count1
        yield count2
        
if __name__ == '__main__':
    t= int(input())
    ans = erase()
    print(*ans,sep='\n')
            
