names =["Mary","John","Emma"]
heights =[180,165,170]
move = True
while move:
    move = False
    for i in range(len(heights)-1):
        if heights[i] < heights[i+1]:
            heights[i], heights[i+1] = heights[i+1], heights[i]
            names[i], names[i+1] = names[i+1], names[i]
            move = True       
#print(heights)
print(names)

# time 10