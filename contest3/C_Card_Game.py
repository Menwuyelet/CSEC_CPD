n = int(input())

for i in range(n):
    a,b,c,d = map(int, input().split())
    count = 0
    if (a>c and b>=d) or (a>=c and b>d):
        count +=1
    if (a>d and b>=c) or (a>=d and b>c):
        count +=1
    if (b>c and a>=d) or (b>=c and a>d):
        count +=1
    if (b>d and a>=c) or (b>=d and a>c):
        count +=1

    print(count)