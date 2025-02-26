n = list(map(int, input().split()))

count = 1
con = True

while con:
    if (n[0]*count) % 10 == 0:
        break
    elif ((n[0]*count) - n[1]) % 10 != 0:
        count += 1
    else:
        con = False
        break
    
print (count)
