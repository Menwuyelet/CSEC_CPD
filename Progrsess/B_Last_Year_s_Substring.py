n = int(input())
tar = "2020"
for i in range(n):
    x = int(input())
    s = input()
    if tar in s:
        print("YES")
    elif s[0] == "2" and s[-3:] == "020":
        print("YES")
    elif s[:2] == "20" and s[-2:] == "20":
        print("YES")
    elif s[:3] == "202" and s[-1] == "0":
        print("YES")
    else:
        print("NO")