t = int(input())
for i in range(t):
    p = int(input())
    s = input()
    w = list(map(int, s.split()))
    if p <= 2:
        print(-1)
    else:
        w.sort()
        x = p//2
        z = w[x]
        su = sum(w)
        av = su/p
        if z < av/2:
            print(0)
        else:
            y = (2*p)*(z) - su
            print(y+1)
