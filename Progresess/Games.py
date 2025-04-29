n = int(input(""))
count = 0
h = []
a = []

for i in range (n):
    g = list(map(int, input("").split()))
    h.append(g[0])
    a.append(g[1])

for i in range (n):
    for j in range(n):
        if i != j and h[i] == a[j]:
            count +=1
    
print (count)
