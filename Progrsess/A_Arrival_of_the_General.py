n = int(input())
solid = list(map(int, input().split()))
tall = max(solid)
short = min(solid)

tall_current = solid.index(tall)
short_current = 0
for i in range(n):
    if short == solid[i]:
        short_current = i
ans = 0
if tall_current > short_current:
    ans = (tall_current + ((n-1) - short_current)) - 1
else:
    ans = tall_current + ((n-1) - short_current)

print(ans)