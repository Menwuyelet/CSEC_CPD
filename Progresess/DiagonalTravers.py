mat =[[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
m = len(mat[0])
diagonal = [[] for _ in range(m+n-1)]
ans = []
for i in range(n):
    for j in range(m):
        diagonal[i+j].append(mat[i][j])
        
for i in range(len(diagonal)):
    if i%2 == 0:
        ans += diagonal[i][::-1]
    else: 
        ans += diagonal[i]
print(ans)