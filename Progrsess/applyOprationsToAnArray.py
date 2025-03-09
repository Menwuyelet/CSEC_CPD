nums = list(map(int, input().split()))

for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i+1] = 0

read = 0
for read in range(len(nums)):
    if nums[read] == 0:
        nums.append(0)
        nums.remove(nums[read])
    else:
        read +=1

print(nums)