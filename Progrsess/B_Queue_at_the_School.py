n , t = map(int,input().split())
s = list(input())
for k in range (t):
    f = 1
    b = 0
    while f < n:
        if s[b] == "B" and s[f] == "G":
            s[b] , s[f] = s[f], s[b]
            b +=2
            f +=2
        else:
            b +=1
            f +=1
print("".join(s))