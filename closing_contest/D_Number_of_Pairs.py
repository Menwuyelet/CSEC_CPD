t = int(input())
for _ in range(t):
    n, r, l = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    av = set(nums)
    for i in nums:
        maxi = r - i
        mini = l - i
        while maxi not in av:
            maxi -= 1
        while mini not in av:
            mini += 1
        
