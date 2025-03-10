img = [[100,200,100],[200,50,200],[100,200,100]]
#img = [[1,1,1],[1,0,1],[1,1,1]]
n = len(img)
m = len(img[0])
ans = [[0]*m for _ in range(n)]

for r in range(n):
    for c in range(m):
        tem = 0
        count = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i < 0 or i == n or j < 0 or j == m:
                    continue
                tem += img[i][j]
                count +=1
        ans[r][c] = tem//count

for i in ans:
    print(i)