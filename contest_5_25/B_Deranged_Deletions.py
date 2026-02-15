t = int(input())
for i in range(t):
    n = int(input())
    nums = list(input().split())
    c = nums.copy()
    c.sort()
    j = 0
    ans = []
    for i in range(len(c)):
        if nums[i] != c[j]:
            ans.append(nums[i])
        j += 1
    if len(ans) == 0:
        print("NO")
    else:
        print(len(ans))
        ans.remove('5')
        print(*ans)
