n = int(input())
freinds = list(map(int, input().split()))

ans = [0 for i in range(n)]

for _ in freinds:
    ans[_ - 1] = freinds.index(_)+1
print(*ans)
