money = int(input())
ans = 0

if money >= 100:
    ans += money//100
    money %= 100 
if money >=20:
    ans += (money//20)
    money %=20
if money >= 10:
    ans+=money//10
    money %= 10
if money >= 5:
    ans+=money//5
    money %= 5
if money >= 1:
    ans +=money
    money %= 1
print(ans)