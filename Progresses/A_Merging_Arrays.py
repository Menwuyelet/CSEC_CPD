n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))
ans = []
a = 0
b = 0

while a < n and b < m:
    if narr[a] <=  marr[b]:
        ans.append(narr[a])
        a += 1
    else:  
        ans.append(marr[b])
        b+=1
ans.extend(marr[b:])
ans.extend(narr[a:])
print(*ans)