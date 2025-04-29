ls = list(map(int,input().split()))
target = int(input())
ans = []
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i] + ls[j] == target:
            ans.append(i)
            ans.append(j)
            break
print(ans)