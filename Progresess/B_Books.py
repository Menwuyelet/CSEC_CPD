n, t = map(int, input().split())
books = list(map(int, input().split()))
c_time = 0
left = 0
ans = 0

for right in range(n):
    c_time += books[right]
    while c_time > t:
        c_time -= books[left]
        left += 1
    ans = max(ans, right-left+1)
    
print(ans)


