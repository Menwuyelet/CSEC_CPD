n = int(input())
word = input().lower()

lis = list(word)
se = set(lis)

if len(se) < 26:
    print("NO")
else:
    print("YES")