t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(1, n**2+1):
        i_n = i + n
        n_i = i - n
        n_ = i + 1
        _n = i - 1
        if i_n > n**2:
            i_n = 0
        if n_i <= 0:
            n_i = 0
        if i % n == 0:
            n_ = 0
        if i % n == 1:
            _n = 0
        # print(i, i_n, n_i, n_, _n)
        ans = max(ans, (i+i_n+n_i+n_+_n))
        # print(ans)
    print(ans)