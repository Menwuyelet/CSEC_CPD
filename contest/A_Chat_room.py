

#print(s)
"""
if "h" not in s or s.index("h") + 1 > len(s)-4:
    print("NO")
   # print("H  ")
elif "e" not in s or s.index("e") + 1 > len(s)-3:
    print("NO")
   # print("E  ")
elif s.count("l") < 2 or s.index("l") + 1 > len(s)-2:
    print("NO")
   # print("l  ")
elif "o" not in s or s.index("o") + 1 > len(s)-1:
    print("NO")
    #print("o  ")
elif "e" not in s[s.index("h"):] or "l" not in s[s.index("e"):] or "o" not in s[s.index("l"):]:
    print("NO")
else:
    print("YES")
"""
s = list(input())
h = {"h","e","l","l","o"}

x = ""

for _ in s:
    if _ in h:
        x += _
ans = {}
i = 0
while i <= len(x)-1:
    if x[i] == "h" and len(ans) == 0:
        ans["h"] = 1
        i+=1
    elif x[i] == "e" and len(ans) == 1:
        ans["e"] = 1
        i+=1
    elif x[i] == "l" and len(ans) == 2  and "l" not in ans :
        ans["l"] = 1
        i +=1
    elif x[i] == "l" and len(ans) == 3 and ans["l"] == 1:
        ans["l"] +=1
        i +=1
    elif x[i] == "o" and len(ans) == 3 and ans["l"] == 2:
        ans["o"] = 1
        i+=1
    else:
        i+=1
    #print(x[i])
#print(s)  
#print(ans)
if "h" in ans and "e" in ans and "l" in ans and ans["l"] == 2 and "o" in ans:
    print("YES")
else:
    print("NO")
