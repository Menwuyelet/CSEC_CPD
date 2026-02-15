n , q = map(int, input().split())
nums = list(input().split())
nums.sort(reverse=True)
summ = []
summ.append(int(nums[0]))

for i in range(1, n):
    summ.append(summ[i-1] + int(nums[i]))
summ = [0] + summ
for i in range(q):
    x, y = map(int, input().split())
    j = x - y
    ans = summ[x] - summ[j]

    print(ans)
