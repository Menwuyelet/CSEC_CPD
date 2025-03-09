n = int(input())
k = int(input())

ls = list(range(1,n+1))
count = 0
while len(ls) > 1:
    if count < k-1:
        ls.append(ls[0])
        ls.remove(ls[0])
        count += 1
    elif count == k-1:
        ls.remove(ls[0])
        count = 0
    
print(ls)