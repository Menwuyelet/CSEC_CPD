n = int(input())
name = {"T", "i", "m", "u", "r"}
for i in range(n):
    x = int(input())
    y = set(input(""))
    if x != len (name):
        print("NO")
    else:
        z = name.union(y) 
        if len(z) > 5:
            print("NO")
        else:
            print("YES")
    
