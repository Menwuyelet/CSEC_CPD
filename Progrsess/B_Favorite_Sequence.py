t = int(input())
ans = []
for i in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    left, right = 0, n-1
    tem = []
    trigh = True
    while left <= right:
        if trigh:
            tem.append(lis[left])
            left +=1
            trigh = False
        else:
            tem.append(lis[right])
            right -=1
            trigh = True
    ans.append(tem)
for _ in ans:
    print(*_)