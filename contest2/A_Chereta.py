#Menwuyelet_ICPC_Temesgen
n = int(input())
li = list(map(int, input().split()))

x = sorted(li)

val = x[-2]
p = li.index(x[-1]) + 1
print(p, val)