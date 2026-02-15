import bisect
t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    x = input()
    sugar = list(map(int, x.split()))
    sugar.sort(reverse=True)
    su = [0]
    for i in sugar:
        su.append(su[-1] + i)

    for i in range(q):
        z = int(input())
        y = bisect.bisect_left(su, z)

        if y < len(su):
            # print(su)
            print(y)
        else:
            
            print(-1)


