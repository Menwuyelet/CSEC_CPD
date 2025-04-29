##Menwuyelet_CSEC_10

n = int(input())
n1 = list(map(int, input().split()))
count1 = 0
count2 = 0 
count3 = 0
for ch in n1:
    if ch == 1: 
        count1 +=1
    elif ch == 2:
        count2 +=1
    elif ch == 3:
        count3 +=1

print(len(n1)-max(count1,count2,count3))
