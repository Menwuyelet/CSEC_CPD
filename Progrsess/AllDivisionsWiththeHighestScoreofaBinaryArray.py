nums = [0,0,1,0]
maxi = 0
ans = 0

zero = nums.count(0)
one = nums.count(1)
if zero == len(nums) or one == len(nums):
    print(ans)
    print("equal")
else:
    val = 0
    i = 0
    count = 0
    while nums[i] == val:
        print("ex")
        count += 1
        i += 1
    val = 1
    print(count)
    if maxi == count:
        ans += 1
    else:
        maxi = max(maxi,count)
        print("assign")

    print(ans)