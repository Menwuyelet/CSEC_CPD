nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
k  = 7
hold = 0
seek = 0
count = 0
for hold in range(len(nums) - 1):
    for seek in range(hold+1, len(nums)):
        if nums[hold] == nums[seek] and (hold*seek)%k == 0:
            count +=1
            
print(count)
