t = int(input())
for i in range(t):
    s = input()
    if len(s) == 1:
        print(s)
    else:
        f, b = 0, 1
        ans = []
        while b < len(s):
            if s[f] != s[b]:
                ans.append(s[f])
                f += 1
                b +=1
            else:
                f +=2
                b +=2
        if f == len(s)-1 and b == len(s):
            ans.append(s[b-1])
        ans.sort()
        j = set(ans)
        ans1 = list(j)
        ans1.sort()
        print("".join(ans1))