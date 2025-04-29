s = input()
pr = 0
se = 1
count = 0
for se in range(len(s)):
    if s[pr] == s[se]:
        count += 1
        se +=1
    else:
        pr = se
        se +=1
        count = 1
    if count >=7:
        print("YES")
        break

if count < 7:
    print("NO")