from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    count = Counter()
    for j in range(n):
        s = input()
        count += Counter(s)
    for i in count:
        if count[i]%n != 0:
            print("NO")
            break
    else:
        print("YES")