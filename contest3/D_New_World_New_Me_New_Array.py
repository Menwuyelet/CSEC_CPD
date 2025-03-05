num = int(input())

for i in range(num):
    n, k, p = map(int,input().split())

    if n*p < abs(k):
        print(-1)
    else:
        rem = abs(k)%p
        if rem == 0:
            print(abs(k)//p)
        else:
            print((abs(k)//p)+1)