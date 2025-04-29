n, m = map(int, input().split())
tas = list(map(int, input().split()))
ch = 1
time = 0
for i in tas:
    if i > ch:
        time += i - ch
        ch = i
    elif i < ch:
        time += (n-ch)+i
        ch = i
    else:
        time +=0
print(time)