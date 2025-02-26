#Menwuyelet_ICPC_Temesgen
n, m = map(int, input().split())
co = []
ans = ""

for i in range(n):
    li = list(input())
    ch = set()
    if  n == 1 or m == 1:
        ans = "NO"
        break
    for _ in li:
        ch.add(_)
    x = len(ch)
    if x > 1:
        ans = "NO"
        break
    else:
        if len(co) >= 1 and li[0] == co[i-1]:
            ans = "NO"
            break
        else:
            co.append(li[0]) 
    ans = "YES"

print(ans)