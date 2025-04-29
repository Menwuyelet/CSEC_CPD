ls = list(map(int, input().split()))

read = 0

for read in range(len(ls)):
    if ls[read] == 0:
        ls.append(0)
        ls.remove(ls[read])
    else:
        read +=1
print(ls)