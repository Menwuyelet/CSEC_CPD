names =["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights =[17233,32521,14087,42738,46669,65662,43204,8224]
sorheights = [heights[0]]
move = True
for i in range(1, len(heights)):
    key = heights[i]
    j = i - 1
    while j >= 0 and key > heights[j]:
        heights[j+1] = heights[j]
        j -= 1
    heights[j+1] = key
    names[j+1] = names[heights[i]]
    

print(names)
print (heights)


