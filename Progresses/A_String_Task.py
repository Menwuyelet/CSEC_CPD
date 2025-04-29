s = input()
vou = {"a", "e", "i", "o", "u", "y"}
ans = []
for _ in s:
    if _.lower() not in vou:
        ans.append("."+ _.lower())

an = "".join(ans)
print(an)