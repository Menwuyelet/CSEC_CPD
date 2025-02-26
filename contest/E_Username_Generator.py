##Menwuyelet_CSEC_10

n = int(input(""))
db = {}
ans = []
for i in range(n):
    x = input("")
    if x in db:
        db [x] +=1
        ans.append(f"{x}{db[x]}")
    else:
        db[x] = 0
        ans.append("OK")
for _ in ans:
    print(_)

"""
due to the while loop it takes O(n^2) time complexity while the above one takes only O(n)
n = int(input(""))
db = set()
ans = []
for i in range(n):
    tem = input("")
    t = tem
    j = 1
    while tem in db:
        tem = t+str(j)
        j +=1
    db.add(tem)
    if j > 1:
        ans.append(tem)
    else:
        ans.append("OK")
for _ in ans:
    print(_)
    """