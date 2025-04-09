q = int(input())
for _ in range(q):
    s1 = input()
    s2 = input()
    ans = 0
    if len(s1) > len(s2):
        i = 0
        while i < len(s2):
            if s1[i] == s2[i]:
                ans += 1
            else:
                break
            i +=1
        if ans != 0:
            ans += 1
        ans += len(s1[i:]) + len(s2[i:])


    elif len(s2) > len(s1):
        i = 0
        while i < len(s1):
            if s1[i] == s2[i]:
                ans += 1
            else:
                break
            i += 1
        if ans != 0:
            ans += 1
        ans += len(s1[i:]) + len(s2[i:])


    else: 
        i = 0
        while i < len(s2):
            if s1[i] == s2[i]:
                ans += 1
            else:
                break
            i += 1
        if ans != 0:
            ans += 1
        ans += len(s1[i:]) + len(s2[i:])
    print(ans)