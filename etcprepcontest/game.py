s = input()

formateds = "".join(s.split())

if formateds[-2].capitalize() in ["A", "E", "I", "O", "U", "Y"]:
    print("YES")
else:
    print("NO")
