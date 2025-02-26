##Menwuyelet_CSEC_10
"""
n, m = map(int, input().split())
h = list(map(int, input().split()))
 
sc = []
pr = 1
tem = 1
for se in range(len(h)-1):
    if h[se] != h[pr]:
        tem += 1
    else:
        tem = 1
    sc.append(tem)
    pr += 1    
print(*sc)
print(max(sc))

"""
n, m = map(int, input().split())
h = list(map(int, input().split()))
 
sc = []
pr = 1
tem = 1
for se in range(len(h)-1):
    if pr < len(h) and h[se] != h[pr]:
        tem += 1
    if pr >= len(h) or h[se] == h[pr] or se == len(h)-2:
        sc.append(tem)
        tem = 1
    pr += 1    
print(max(sc))




"""n, m = map(int, input().split())
h = list(map(int, input().split()))
 
sc = []
tem = 0
 
for i in range(len(h)-1):
    if i+1 < len(h):
        if h[i] == h[i+1]:
            tem = 1
        elif h[i]!= h[i+1]:
            tem +=1
        if tem == (len(h)-1):
            sc.append(tem+1)
        else:
            sc.append(tem)
    else:
        break
    
print(max(sc))
"""