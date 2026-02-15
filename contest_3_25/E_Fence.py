n, k = map(int, input().split())
nums = list(map(int, input().split()))
l, r = 0, k
start = sum(nums[l:r])
total = start
ans = 0
while r < n-1:
    l+=1
    start -= nums[l-1]
    start += nums[r]  
    r+=1  

    if total > start:
        ans = l+1

print(ans)