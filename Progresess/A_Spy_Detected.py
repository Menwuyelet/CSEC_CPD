t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    num1 = []
    num2 = []
    for i, num in enumerate(nums):
        if len(num1) == 0 and len(num2) == 0:
            num1.append((num, i+1))
        elif num == num1[0][0]:
            num1.append((num, i+1))
        else:
            num2.append((num, i+1))
    ans = num1[0][1] if len(num1) == 1 else num2[0][1]
    print(ans)