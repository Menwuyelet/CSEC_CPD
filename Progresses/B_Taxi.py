"""n = int (input())
s = list(map(int, input().split()))
front = 0
last = n-1
taxi = n
s.sort(reverse=True)
while front < last:
    if s[front] + s[last] == 4:
        taxi -=1
        front +=1
        last -= 1
    elif s[front] + s[last] > 4:
        front +=1
    elif s[front] + s[last] < 4:
        last -=1

print(taxi)"""

n = int(input())
s = list(map(int, input().split()))
front = 0
last = n-1
s.sort(reverse=True)
tem = 0

while front < last:
    while front < n and s[front] < 4:
        if s[front] + s[last] <= 4 and front < last:
            s[front] += s[last]
            s[last] = 0
            last -=1
        else:
            break
    front +=1

print( n - s.count(0))



