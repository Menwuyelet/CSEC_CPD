arr = list(map(int, input().split()))
left = 0
right = 1
ans = "true"
while right < len(arr):
    if arr[left] > arr[right]:
        ans = "false"
        break
    else:
        left +=1
        right +=1
print(ans)