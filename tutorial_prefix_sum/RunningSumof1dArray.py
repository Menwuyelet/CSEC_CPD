nums = [1, 2, 3, 4]
sum = []
sum.append(nums[0])
for i in range(1, len(nums)):
    sum.append(sum[i-1] + nums[i])
print(sum)