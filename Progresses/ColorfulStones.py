s = list(input(""))
s1 = list(input(""))

i = 1
if s == s1:
    i+= len(s) - 1
else:
    for j in s1:
        if s[i-1] == j:
            i+=1
print(i)
