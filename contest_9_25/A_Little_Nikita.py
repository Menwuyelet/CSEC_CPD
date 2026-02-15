t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b and ((a-b)%2) == 0:
        print("Yes")
    elif a == b:
        print("Yes")
    else:
        # print(a-b)
        print("No")