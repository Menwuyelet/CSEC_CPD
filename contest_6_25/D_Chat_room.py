from collections import Counter
s = input()
freq = {1 : 'h', 2: 'e', 3: 'l', 4:'l', 5:'o'}
i = 1
j = 0
ans = ""
while i < 6 and j < len(s):
    if s[j] == freq[i]:
        ans += freq[i]
        i += 1
        j += 1
    else:
        j+=1

if ans == "hello":
    print("YES")
else:
    print("NO")
# print(ans)