n = int(input())
for i in range(n):
    x = int(input())
    if x%3 == 0 or x%7 == 0:
        print("YES")
    elif x == 