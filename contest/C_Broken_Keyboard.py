t = int(input())
for i in range(t):
    s = list(input())
    if len(s) == 1:
        print(*s)
    else:
        coun = {}
        for i in s:
            if i in coun:
                coun[i] +=1
            else:
                coun[i] = 1
        x = []
        for _ in s:
            if coun[_]%2 != 0:
                x.append(_)
                coun[_] = 2
            else:
                if s[s.index(_) + 1] != _ and _ not in x:
                    x.append(_)
        x.sort()
        y = "".join(x)
        print(y)

"""    else:
        left, right = 0, 1
        while right < len(s):
            if s[left] == s[right]:
                s[left] = " "
                s[right] = " "
            left +=1
            right +=1
        s.sort()
        x = "".join(s)
        y = x.replace(" ", "")
        print(y)"""
    

