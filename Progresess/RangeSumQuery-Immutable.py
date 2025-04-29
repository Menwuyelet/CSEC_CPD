class NumArray:
    def __init__(self, nums):
        self.sum_num = [0]
        current_sum = 0
        for i in nums:
            self.sum_num.append(current_sum+i)
            current_sum += i
    def sumRange(self, left: int, right: int) -> int:
       return self.sum_num, (self.sum_num[right+1] - self.sum_num[left]), self.sum_num[right], self.sum_num[left]
    

        
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))