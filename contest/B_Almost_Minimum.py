##Menwuyelet_CSEC_10

n = int(input())
n1 = set(map(int, input().split()))
x = list(n1)
x.sort()
if len(x) > 1:
    print(x[1])
else:
    print("NO")