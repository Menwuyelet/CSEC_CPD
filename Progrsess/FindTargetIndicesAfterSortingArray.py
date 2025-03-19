nums = [1,2,5,2,3]
target = 2

nums.sort()
count = nums.count(target)
ans = []
for i in range(count):
    ans.append(nums.index(target)+i)

print(ans)

## time 6minu