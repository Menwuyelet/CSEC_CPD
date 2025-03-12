n = int(input())
nums = list(map(int, input().split()))
ans = []
su = sum(nums)
for i in range(n):
    if nums[i]*(n-1) == su-nums[i]:
        ans.append(i+1)
    
print(len(ans))
print(*ans)