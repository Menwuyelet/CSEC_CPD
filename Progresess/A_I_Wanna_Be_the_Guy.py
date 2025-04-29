n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x[0] = 0
y[0] = 0
tot = x+y

setot = set(tot)

if len(setot)-1 == n:
    print("I become the guy.") 
else:
    print("Oh, my keyboard!")