img = [[100,200,100],[200,50,200],[100,200,100]]
#img = [[1,1,1],[1,0,1],[1,1,1]]
n = len(img)
m = len(img[0])
ans = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        min_row = max(i-1, 0)
        min_column = max(j-1, 0)
        max_row = min(i+1, n-1)
        max_column = min(j+1, m-1)
        sum, count = 0, 0
        for r in range(min_row, max_row+1):
            for c in range(min_column, max_column+1):
                sum += img[r][c]
                count +=1
        ans[i][j] = sum//count
for i in ans:
    print(i)
















"""for r in range(n):
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
    print(i)"""
