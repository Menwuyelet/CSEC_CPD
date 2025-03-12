arr = list(map(int, input().split()))
m = int(input())

sum = sum(arr[:m])
tot = 0
for i in range(len(arr)-m):
    tem = sum - arr[i]
    tem += arr[i+m]
    tot = max(tot, tem)
print(tot/m)
