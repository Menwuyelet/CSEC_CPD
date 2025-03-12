n = int(input())
count = 0
for i in range(n):
    lis = list(map(int, input().split()))
    if lis.count(0) < 2:
        count +=1
    
print(count)
