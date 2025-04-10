t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    count_white = s[:k].count("W")
    min_white = count_white

    for i in range(k, n):
        if s[i-k] == "W":
            count_white -= 1
        if s[i] == "W":
            count_white += 1
        min_white = min(min_white, count_white)
    print(min_white)