# n , k = map(int, input().split())
# nums = list( map(int, input().split()))

# i = j = 0
# sum = 0
# while i <= n-k and j < n:
#     tem = 0
#     while j - i < k:
#         tem += nums[j]
#         j += 1
#     i = j
    
#     sum += tem

# #print(sum)
# ans = sum/(n - k + 1)
# print(ans)


n, k = map(int, input().split())
nums = list(map(int, input().split()))

sum = sum(nums[:k])
totalSum = sum
i = k
while i < n:
    sum  += nums[i] - nums[i-k]
    totalSum += sum 
    i += 1
#print(totalSum)
ans = totalSum/ (n - k + 1)
print(f"{ans:.10f}")