matrics = [["a0", "a1", "a2", "a3"], ["b0", "b1", "b2", "b3"], ["c0", "c1", "c2", "c3"], ["d0","d1", "d2", "d3"]]
row = 0
column = 0
new_arr = [0]*16

for row in range(len(matrics)):
    for column in range(len(matrics[0])):
        if row + column == len(matrics[0])-1:
            print(matrics[row][column])
#print(new_arr)