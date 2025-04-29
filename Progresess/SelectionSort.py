arr = [4, 1, 3, 9, 7]
n = len(arr)
for i in range(n):
    indx = i
    for j in range(i+1, n):
        if arr[indx] > arr[j]:
           indx = j

    arr[i], arr[indx] = arr[indx], arr[i]
        

print(*arr)