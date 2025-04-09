t = int(input())
for _ in range(t):
    n = int(input())
    el = list(map(int, input().split()))
    el.sort()
    cost = 0
    left = 0
    right = n-1
    while left <= right:
        cost += el[right] - el[left]
        left +=1
        right -= 1
    print(cost)