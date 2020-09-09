from collections import deque
import sys
input = sys.stdin.readline
 
 
def get_diameter(tree):
    u, _, _ = _dfs(0, tree)
    v, diam, dist = _dfs(u, tree)
 
    path = [v]
    while v != u:
        for nxt_v in tree[v]:
            if 1 + dist[nxt_v] == dist[v]:
                path.append(nxt_v)
                v = nxt_v
                break
    return diam, path
 
 
def _dfs(start, tree):
    n = len(tree)
    dist = [-1] * n
    dist[start] = 0
    stack = [start]
    while stack:
        v = stack.pop()
        for nxt_v in tree[v]:
            if dist[nxt_v] != -1:
                continue
            dist[nxt_v] = dist[v] + 1
            stack.append(nxt_v)
    max_d = max(dist)
    return dist.index(max_d), max_d, dist
 
 
def ab(a, b):
    INF = 10 ** 6
    visited = [INF] * n
    visited[a] = 0
    q = deque([a])
    while q:
        v = q.popleft()
        for nxt_v in tree[v]:
            if visited[v] + 1 < visited[nxt_v]:
                visited[nxt_v] =  visited[v] + 1
                q.append(nxt_v)
    return visited[b]
 
 
t = int(input())
for _ in range(t):
    n, a, b, da, db = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    
    a -= 1
    b -= 1
    if da * 2 >= db:
        print("Alice")
        continue
        
    tree = [[] for i in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    
    distance = ab(a, b)

    if distance <= da:
        print("Alice")
        continue
 
    d, _ = get_diameter(tree)
 
    if d >= da*2+1:
        print("Bob")
    else:
        print("Alice")
