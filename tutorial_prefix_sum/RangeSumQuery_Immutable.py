class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = []
        self.sum.append(self.nums[0])
        for i in range(1, len(nums)):
            self.sum.append(self.sum[i-1] + self.num[i])
    def sumRange(self, left: int, right: int) -> int:
        return(self.sum[right]-self.sum[left-1])