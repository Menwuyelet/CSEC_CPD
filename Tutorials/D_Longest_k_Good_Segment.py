from collections import defaultdict
n, k = map(int, input().split())
lis = list(map(int, input().split()))
chr_count = 0
ans = [[0,0], 1]
front = back = 0
seen = defaultdict(int)
while back < n:
    if seen[lis[back]] == 0:
        seen[lis[back]] += 1
        chr_count += 1
    else:
        seen[lis[back]] += 1
    if chr_count < k:
        back += 1

    
    if chr_count > k:
        if ans[1] < chr_count:
            ans = [[front + 1, back + 1], chr_count]
    
    while chr_count > k and front <= back:
        seen[lis[front]] -= 1
        if seen[lis[front]] == 0:
            chr_count -= 1
        front += 1

print(*ans[0])