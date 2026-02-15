n, m = map(int, input().split())
lis = list(range(n))

for i in range(m):
    hint = input()
    left = len(lis)-1
    right = 0
    if "To the right of" in hint:
        right = int(hint[-1]) 
    elif "To the left of" in hint:
        left = int(hint[-1])

lis = lis[right:]
lis = lis[:left]

if len(lis) != 0:
    print(len(lis))
else:
    print(-1)