t = int(input())
for i in range(t):
    n = input()
    nums = input().split()
    left, right = 0, int(n)-1
    while left < right:
        if int(nums[left]) > int(nums[right]):
            x = int(nums[right])
            right -= 1
            if x > int(nums[right]):
                print("NO")
                break
        elif int(nums[right]) > int(nums[left]):
            x = int(nums[left])
            left += 1
            if x > int(nums[left]):
                print("NO")
                break
    else:

        print("YES")