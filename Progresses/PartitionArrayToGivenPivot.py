nums = [9,12,5,10,14,3,10]
pivot = 10
tar = []
les = []
gret = []

for i in nums:
    if i < pivot:
        les.append(i)
    elif i > pivot:
        gret.append(i)
    else:
        tar.append(i)
    

print(les+tar+gret)