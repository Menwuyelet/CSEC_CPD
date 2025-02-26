w = input("")
up = 0
dn = 0
for ch in w:
    if ch == ch.upper():
        up +=1
    else:
        dn +=1
if up > dn:
    print(w.upper())
else:
    print(w.lower())
