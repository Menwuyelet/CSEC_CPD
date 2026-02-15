class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.summ = [[0 for _ in range(len(matrix)+1)] for _ in range(len(matrix[0])+1)]
        self.summ[1][1] = matrix[0][0]
        for i in (1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.summ[i][j] =  self.summ[i−1][j] + self.summ[i][j−1] − self.summ[i−1][j−1] + self.summ[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.summ[row2][col2] − self.summ[row2][col1 - 1] - self.summ[row1 - 1][col2 ] + self.summ[row1 - 1][col1 - 1])