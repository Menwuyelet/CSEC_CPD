n = int(input())

for i in range(n):
    rounds = list(map(int, input().split()))
    sev = 0
    cont = 0
    if rounds[0] > rounds[2]:
        cont +=1
    if rounds[0] > rounds[3]:
        cont +=1
    if rounds[1] > rounds[2]:
        cont +=1
    if rounds[1] > rounds[3]:
        cont +=1
    if cont == 4:
        sev = 4
    elif cont == 3 :
        sev = 2
    elif cont == 2:
        sev = 1
    elif cont == 1  or cont == 0:
        sev = 0


    print(sev)