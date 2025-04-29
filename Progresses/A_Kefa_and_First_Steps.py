n = int(input())
s = list(map(int,input().split()))

front = 1
count = []
tem = 1
if n == 1:
    count.append(1)
else:
    for back in range(n-1):
        if front < n and s[back] <= s[front]:
            tem += 1
        if front > n or s[back] > s[front] or back == (n-2):
            count.append(tem)
            tem = 1
        front +=1

print(max(count))