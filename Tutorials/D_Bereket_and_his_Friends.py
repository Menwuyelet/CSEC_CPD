s = input()
m = int(input())
sum = [0]
current = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        sum.append(current+1)
        current += 1
    else:
        sum.append(current)
for i in range(m):
    a, b = map(int, input().split())
    print(sum[b-1]-sum[a-1])