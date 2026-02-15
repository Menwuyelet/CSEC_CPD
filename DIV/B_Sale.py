n, m = map(int, input().split())
tvs = [int(num) for num in input().split()]

tvs.sort()
ans = 0
count = 0

for tv in tvs:
    if count < m and tv <= 0:
        ans -= tv
        count += 1
    else:
        break
print(ans)