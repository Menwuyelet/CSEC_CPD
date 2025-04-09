t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    count = 0
    i = 0
    if n == k:
        while i < n:
            temp = 0
            j = i
            if s[i] == "B":
                while j < n:
                    if s[j] == "B":
                        temp+=1
                    j+=1
            i+=1
            count = max(count, temp)
    else:
        while i < n-k:
            temp = 0
            j = i
            if s[i] == "B":
                while j < i+k:
                    if s[j] == "B":
                        temp+=1
                    j+=1
            i+=1
            count = max(count, temp)

    if k < count:
        print(0)
    else:
        print(k-count)