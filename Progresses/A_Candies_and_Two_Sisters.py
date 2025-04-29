t = int(input())
for i in range(t):
    candy = int(input())
    if candy == 1 or candy == 2:
        print(0)
    else:
        if candy % 2 == 0:
            ans = candy - ((candy//2)+1)
            print(ans)
        else:
            ans = candy - ((candy//2)+1)
            print(ans)