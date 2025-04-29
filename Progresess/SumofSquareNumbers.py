import math

c = 3
k = int(math.sqrt(c))
ls =  [_ for _ in range(k+1)]
left = 0
right = k
ans = "false"
while left <= right:
    if pow(ls[left], 2) + pow(ls[right], 2) == c:
        ans = "true"
        break
    elif pow(ls[left], 2) + pow(ls[right], 2) > c:
        right -= 1
    else:
        left += 1

print(ans)

# solved with in 45 minutes