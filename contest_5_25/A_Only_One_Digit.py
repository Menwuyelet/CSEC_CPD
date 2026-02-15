t = int(input())
for i in range(t):
    x = input()
    if len(x) == 1:
        print(x)
    else:
        y = list(x)
        print(min(y))
