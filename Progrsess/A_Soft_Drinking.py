n, k, l, c, d, p , nl, np = map(int, input().split())
td = k*l
ts = c*d

dtd = td // (n*nl)
dts = ts//n
dp = p//(n*np)
print(min(dtd, dts, dp))