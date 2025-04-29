from collections import defaultdict
s = "eccbbbbdec"
val = defaultdict(int)
for i in range(len(s)):
    val[s[i]] = i
size = 0
last_C = 0
ans = []
for i in range(len(s)):
    last_C = max(last_C, val[s[i]])
    size += 1
    if last_C == i:
        ans.append(size)
        size = 0

print(ans)

