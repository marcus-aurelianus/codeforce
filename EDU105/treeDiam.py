import collections 
def treeDiameter(edges) -> int:
    g, res = collections.defaultdict(list), 0
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    def dfs(cur, pre):
        nonlocal res
        d1 = d2 = 0
        for i in g[cur]:
            if i != pre:
                d = dfs(i, cur)
                if d > d1:
                    d1, d2 = d, d1
                elif d > d2:
                    d2 = d
        res = max(res, d1 + d2)
        print(cur,d1,d2)
        return d1 + 1

    dfs(0, None)
    return res

print(treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
