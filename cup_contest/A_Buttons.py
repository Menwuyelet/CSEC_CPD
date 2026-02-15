t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b:
        if c % 2 == 0:
            print("Second")
        else:
            print("First")
    elif a > b:
        print("First")
    elif a < b:
        print("Second")