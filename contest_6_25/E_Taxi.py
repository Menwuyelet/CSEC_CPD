# from collections import Counter
# n = int(input())
# groups = list(map(int, input().split()))
# count = Counter(groups)
# # print(count)
# ans = 0
# groups.sort()
# for i in groups:
#     # print(4-i)
#     if (4 - i in count.keys()  and count[4-i] > 0) and count[i] > 0:
#         ans+=1
#         count[i] -= 1
#         count[4-i] -= 1
#     elif ( i == 4 or count[4-i] == 0) and count[i] > 0:
#         ans+=1
#         count[i] -= 1
# print(ans)

# n = int(input())
# nums = list(map(int, input().split()))

# ans = 0
# curr_sum = 0

# r = 0
# nums.sort()
# while r < n:
#     if curr_sum + nums[r] <= 4:
#         curr_sum+=nums[r]
#         r += 1
#     elif curr_sum + nums[r] > 4:
#         ans += 1
#         curr_sum = 0


import math
from collections import Counter
n = int(input())
nums = list(map(int, input().split()))

count = Counter(nums)
ans = 0
ans += count[4]
ans += count[3]

if count[1] >= count[3]:
    count[1] -= count[3]
else:
    count[1]=0
ans+=count[2]//2
if count[2]%2==1:
    ans+=1
    if count[1]>=0:
        count[1]-=2
ans += math.ceil(count[1]/4)        

print(ans)
    