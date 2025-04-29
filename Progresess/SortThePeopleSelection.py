names =["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights =[17233,32521,14087,42738,46669,65662,43204,8224]
for i in range(len(heights)):
    mx = i 
    for j in range(i+1, len(heights)):
        if heights[mx] < heights[j]:
            mx = j
    heights[i], heights[mx] = heights[mx], heights[i]
    names[i], names[mx] = names[mx], names[i]
    
print(names)
print(heights)

## time 15minu