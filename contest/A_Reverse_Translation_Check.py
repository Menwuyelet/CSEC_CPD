##Menwuyelet_CSEC_10

s1 = list(input(""))
s2 = list(input(""))
s2.reverse()
ans = "YES"
if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans = "NO"
else:
    ans = "NO"

print(ans)