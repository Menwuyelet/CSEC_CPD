t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    i = 0
    count = 0
    while i < n:
        j = i
        if s[i] != "B":
            i += 1
        else:
            j += k-1
            i = j+1
            count += 1
    print(count)