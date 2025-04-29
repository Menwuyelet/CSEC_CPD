n = int(input())
coins = list(map(int, input().split()))

total = sum(coins)
mini = total/2
coins.sort(reverse=True)
val = 0
count = 0
for i in coins:
    val += i
    count +=1
    if val>mini:
        break

print(count)