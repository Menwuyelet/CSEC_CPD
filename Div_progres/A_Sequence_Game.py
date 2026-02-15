t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(num) for num in input().split()]
    x = int(input())
    i = n - 1
    while i > 0:
        first_num = nums.pop()
        second_num = nums.pop()
        nu = first_num + second_num
        nums.append(nu//2)

        i -= 1
    if nums[0] == x:
        print("YES")
    else:
        print("NO")