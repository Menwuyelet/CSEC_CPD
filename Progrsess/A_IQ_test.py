n = int(input())
nums = list(map(int, input().split()))
even = []
odd = []
for i, num in enumerate(nums):
    if num%2 == 0:
        even.append((num, i+1))
    else:
        odd.append((num, i+1))
ans = even[0][1] if len(even) == 1 else odd[0][1]
print(ans)