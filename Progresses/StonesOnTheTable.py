n = int(input(""))
n1 = list(input())
count = 0
for i in range(n-1):
    if n1[i] == n1[i+1]:
        count +=1

print(count)
