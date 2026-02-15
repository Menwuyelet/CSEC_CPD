num = []
for _ in input():
    if _ != "+":
        num.append(int(_))
    
num.sort()
ans = []
for num in num:
    ans.append(str(num))

print("+".join(ans))