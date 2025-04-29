t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    tot = 0
    i = 0
    j = i
    while i < n:
        if nums[i] > 0:
            tot += nums[i]
            i += 1
        elif nums[i] <= 0:
            temp = 0
            while i < n and nums[i] <= 0:
                if nums[i] < 0:
                    tot+= (-1*nums[i])
                    temp +=1
                i+=1
            if temp:
                count+=1
    print(tot, count)

