t = int(input())
for i in range(t):
    a, b = map(int,input().split())

    if a%b == 0:
        print(0)
    else:
        rem = a%b
        ans = b-rem
        print(ans)