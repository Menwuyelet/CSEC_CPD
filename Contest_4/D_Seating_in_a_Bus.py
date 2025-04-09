t = int(input())
for _ in range(t):
    n = int(input())
    seats = list(map(int, input().split()))
    taken = set()
    ans = "YES"
    for i in seats:
        if len(taken) == 0:
            taken.add(i)
        else:
            if (i-1 not in taken) and (i+1 not in taken):
                ans = "NO"
                break
            taken.add(i)
    print(ans)