
prev_max = float('inf')
for _ in range(int(input())):
    rect = [int(num) for num in input().split()]
    if prev_max >= max(rect):
        prev_max = max(rect)
    elif prev_max >= min(rect):
        prev_max = min(rect)
    else:
        print("NO")
        break
else:
    print("YES")