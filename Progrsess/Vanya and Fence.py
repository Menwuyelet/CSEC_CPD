n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

count  = 0
for i in n2:
    if i > n1[1]:
        count +=2
    else: 
        count +=1

print(count)
