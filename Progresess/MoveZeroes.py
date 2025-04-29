nums = list(map(int, input().split()))
pr = 0
se = 0

for se in range(len(nums)):
    if nums[pr] == 0 and nums[se] != 0:
        nums[pr], nums[se] = nums[se], nums[pr]
        pr +=1
        se +=1
    elif nums[pr] != 0:
        pr +=1
    else:
        se +=1
print(nums)