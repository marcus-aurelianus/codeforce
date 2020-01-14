

n, k = map(int, input().split())
words = []
was = dict()
for i in range(n):
    a = input()
    words.append(a)
    was[a] = i
ans = 0
for i in range(n):
    for i1 in range(i + 1, n):
        s = ''
        for j in range(k):
            a = ['S', 'E', 'T']
            if words[i][j] == words[i1][j]:
                s += words[i][j]
            elif words[i][j] == 'S' and words[i1][j] == 'T':
                s += 'E'
            elif words[i][j] == 'S' and words[i1][j] == 'E':
                s += 'T'
            elif words[i][j] == 'E' and words[i1][j] == 'T':
                s += 'S'
            elif words[i][j] == 'E' and words[i1][j] == 'S':
                s += 'T'
            elif words[i][j] == 'T' and words[i1][j] == 'E':
                s += 'S'
            elif words[i][j] == 'T' and words[i1][j] == 'S':
                s += 'E'
        if s in was:
            if was[s] > i1:
                ans += 1
print(ans)


