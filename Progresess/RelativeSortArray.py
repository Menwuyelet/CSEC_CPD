arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
x = []
for i in arr2:
    for j in arr1:
        if i == j:
            x.append(j)
arr = set(arr2)
arr3 = [i for i in arr1 if i not in arr] 
arr3.sort()
ans = x + arr3
print(ans)

## time 10 min