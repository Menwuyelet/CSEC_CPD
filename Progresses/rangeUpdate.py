nums = [1, 3, 5, 7]
queries = [[1, 2], [2, 1]]

sum = [0] * len(nums)

for index, value in queries:
    sum[index] += value

current = 0
for i in range(len(nums)):
    current += sum[i]
    nums[i] += current
print(sum)
print(nums)