n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
a, b = 0, 0
ans = []
cout = 0
for b in range(len(arr2)):
    while a < n and arr1[a] < arr2[b]:
        a += 1
        cout +=1
    ans.append(cout)
    b+=1
print(*ans)