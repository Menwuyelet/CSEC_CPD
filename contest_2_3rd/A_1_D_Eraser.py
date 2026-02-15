t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    end = 0
    count = 0
    while end < len(s):
        if s[end] == "B":
            while s[end] == "B":
                end += 1
                if end >= len(s):
                    break
            count += 1
        end += 1
    print(count)
