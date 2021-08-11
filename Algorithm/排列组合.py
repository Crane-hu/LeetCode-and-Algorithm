def Anm(n, m):
    res = 1
    plus = n
    while plus > n - m:
        res *= plus
        plus -= 1
    return res

def fac(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

def Cnm(n, m):
    return Anm(n, m) // fac(m)
