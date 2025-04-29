n = int(input(""))
ls = list(map(int, input("").split()))
 
s = 0
d = 0
 
star = 0
end = n - 1
 
serg = True
 
while star <= end:
    if serg:
        if ls[star] >= ls[end]:
            s +=ls[star]
            star += 1
        elif ls[star] < ls[end]:
            s +=ls[end]
            end -=1
        serg = False
    else:
        if ls[star] >= ls[end]:
            d +=ls[star]
            star +=1
        elif ls[star] < ls[end]:
            d +=ls[end]
            end -=1
        serg = True
 
print(s, d)
