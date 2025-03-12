n = int(input())
x = 0
y = 0
z = 0
for i in range(n):
    x1,y1,z1 = map(int,input().split())
    x +=x1
    y +=y1
    z +=z1
if x != 0 or y != 0 or z != 0:
    print("NO")
else:
    print("YES")