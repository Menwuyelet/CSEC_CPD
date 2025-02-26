s = list(input(""))
s1 = set(s)

if len(s1)%2 == 0:
    print("CHAT WITH HER!")
elif len(s1)%2 != 0:
    print("IGNORE HIM!")
