n , m = map(int, input().split())
ls = list(map(int,input().split()))

right = m-2
left = m
count = 0
start = True
r = True
l = True
if n == 1:
    if ls[n-1] == 1:
        count +=1

while right >= 0 or left <= n-1:
    if right < 0:
        r = False
    if left > n-1:
        l = False
    if ls[m-1] == 1 and start:
        count +=1
        start = False
    elif r and l:
        if ls[right] == 1 and ls[left] == 1:
            count +=2
            right -=1
            left +=1
        else:
            right -=1
            left +=1
    elif r and not l:
        if ls[right] == 1:
            count +=1
            right -=1
        else :
            right -=1
    elif l and not r:
        if ls[left] == 1:
            count +=1
            left +=1
        else:
            left +=1

print(count)