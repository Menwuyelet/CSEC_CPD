l = {"A": 0, "B": 0, "C": 0}
visit = []
for i in range(3):
    first = input()
    if first[1] == ">":
        l[first[0]] +=1
    else:
        l[first[2]] += 1

sorted_l = dict(sorted(l.items(), key=lambda item: item[1]))
key = list(sorted_l.keys())
val = list(sorted_l.values())

if len(set(val)) < 3:
    print("Impossible")
else:
    for i in range(3):
        print(key[val[i]], end="")
    
