n = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = n//2
m = n//k
i = 0
count = 0
while i < n:
    j = i+m - 1
    while i < j:
        count += nums[j] - nums[i]
        i += 1
    i = j+1

print(count)