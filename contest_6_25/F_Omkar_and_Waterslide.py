# t = int(input())
# for _ in range(t):
#     n = int(input())
#     nums = list(map(int, input().split()))

#     ans = 0
#     curr_lack = 0
#     maxi = max(nums)
#     for i in range(n-1):
#         if nums[i] < 

limit = 5000

weight = []
def count(weight):
    weight.sort()
    count = 0
    ans = 0
    for item in weight:
        if count + item > limit:
            return ans
        elif count + item == limit:
            return ans + 1
        count += item
        ans += 1
    return ans

print(count(weight))