lst = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]

m,n = min(lst,key=lambda x:[x[0],x[1]])
print(m,n)