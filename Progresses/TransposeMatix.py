matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])
t_matrix = []
for j in range(n):
    row = []
    for i in range(m):
        row.append(matrix[i][j])
    t_matrix.append(row)
        

print(t_matrix) 