n = int(input())
nums = list(map(int, input().split()))
tot = sum(nums)
if tot%3 != 0:
    print(0)
else:
    target = tot//3
    count = 0
    ways = 0
    temp = 0
    for i in range(n-1):
        temp += nums[i]
        if temp == 2*target:
            ways += count
        if temp == target:
            count +=1
    print(ways)  
