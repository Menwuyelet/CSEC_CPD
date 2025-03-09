n = int(input())
k = int(input())

ls = list(range(1, n+1))
idx = 0

while len(ls) > 1:
    rm = (idx + k-1) % len(ls)
    ls.remove(ls[rm])
    idx = rm
print(ls)