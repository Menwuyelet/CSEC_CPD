n = int (input(""))
nums = 0
for i in range(n):
    x = list(map(int, input().split()))
    count = 0
    for ch in x:
        if ch == 1:
            count +=1
    if count > 1:
        nums +=1
    
print (nums)

