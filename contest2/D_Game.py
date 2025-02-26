#Menwuyelet_ICPC_Temesgen
n = int(input())
ans = []
j = 1
t = 0
for i in range(1,n):
    x = j + (t+1)
    t += 1
    if x <= n:
        ans.append(x)
        j = x
    else:
        ans.append(x-n)
        j = x-n
print(*ans)