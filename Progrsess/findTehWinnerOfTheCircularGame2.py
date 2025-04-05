n = int(input())
k = int(input())

# ls = list(range(1, n+1))
# idx = 0

# while len(ls) > 1:
#     rm = (idx + k-1) % len(ls)
#     ls.remove(ls[rm])
#     idx = rm
# print(ls)

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res+1)