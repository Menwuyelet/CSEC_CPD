t = int(input())
for i in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    p = '0'*p1
    z = '0'*p2
    y1 = str(x1) + p
    y2 = str(x2) + z
    # print(y1)
    # print(y2)
    if int(y1) > int(y2):
        print(">")
    elif int(y1) < int(y2):
        print("<")
    else:
        print("=")