nums = [1,2,3,4]
current_sum = 0
ans = []
for i in nums:
    ans.append(current_sum+i)
    current_sum += i
print(ans)