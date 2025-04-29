n = list(map(int, input().split()))
target = int(input())
front = 0
last = len(n) - 1

while front < last:
    if n[front] + n[last] < target:
        front += 1
    elif n[front] + n[last] > target:
        last -=1
    else:
        print("["+str(front + 1)+","+str(last + 1)+"]")
        break