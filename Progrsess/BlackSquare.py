n = list(map(int, input("").split()))
n1 = list(map(int, input("")))

cal = 0

for i in n1:
    cal += n[i-1]

print(cal)
