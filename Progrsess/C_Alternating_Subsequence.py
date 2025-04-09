from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    i = 0
    groups = defaultdict(list)
    while i < n:
        j = i + 1
        while j < n and ((nums[j] > 0) == (nums[i] > 0)):
            j += 1
        groups[i] = nums[i:j]
        i = j
    ans = 0
    for key in groups:
        ans += max(groups[key])
    print(ans)
