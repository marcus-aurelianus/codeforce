def minimumDeletions(s: str) -> int:
    n = len(s)
    ansF = [0]*n
    ansB = [0]*n
    for i in range(n):
        if s[i] == 'b':
            if i==0:
                ansF[i]+=1
            else:
                ansF[i]+=ansF[i-1]+1
        else:
            if i!=0:
                ansF[i]+=ansF[i-1]         
        if s[n-1-i] == 'a':
            if i==0:
                ansB[n-1-i]+=1
            else:
                ansB[n-1-i]+=ansB[n-i]+1
        else:
            if i!=0:
                ansB[n-1-i]+=ansB[n-i]                  
    return min(ansB[i]+ansF[i] for i in range(n))-1

s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"\
#####axaxaaaaxxxxxaaaxa
s1 = 'aababbab'
print(minimumDeletions(s1))

print(s.count('a'))
