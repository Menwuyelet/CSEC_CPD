s = input()
n = int(input())
l = 0
r = 1
valid = set()
while r < len(s):
    if s[l] == s[r]:
        valid.add(l+1)
    r += 1
    l += 1
# print(valid)

for i in range(n):
    a, b = map(int, input().split())
    i = a
    count = 0
    while i < b:
        if i in valid:
            count += 1
        i += 1
    print(count)