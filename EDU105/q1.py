import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        bras = input()
        ans = 'No'
        for target in ['A','B','C']:
            temAns = True
            tem = 0
            for ele in bras:
                if ele == target:
                    tem += 1
                else:
                    tem -= 1
                    if tem<0:
                        temAns = False
                        break
            if tem == 0 and temAns:
                ans = 'Yes'
            temAns = True
            tem = 0
            for ele in bras[::-1]:
                if ele == target:
                    tem += 1
                else:
                    tem -= 1
                    if tem<0:
                        temAns = False
                        break
            if tem == 0 and temAns:
                ans = 'Yes'
                
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
