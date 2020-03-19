def power(base,e):
    res=1
    while e:
        if e%2==1:
            res=res*base%mod;
        base=base*base%mod
        e//=2
    return res
