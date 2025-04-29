n = int(input(""))
n1 = list(map(int, input("").split()))
police = 0
crime = 0
for i in range(n):
    if n1[i] == -1 and police == 0:
        crime +=1
    elif n1[i] ==-1 and police != 0:
        police -=1
    elif n1[i] !=-1:
        police += n1[i]

print (crime)
