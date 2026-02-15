t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    num = []
    for i in s:
        num.append(int(i)-1)
    dic = {0:1}
    sum = 0
    curr = 0
    for i in num:
        curr += i
        if curr in dic:
            sum += 1
            dic[curr] += 1
        else:
            dic[curr] = 1
    print(sum)

            
