boxes = list(input())
ans = []

for i in range(len(boxes)):
    tem = 0
    for j in range(len(boxes)):
        if i!=j and boxes[j] == "1":
            tem += abs((j+1) - (i+1))
    ans.append(tem)

print(ans)