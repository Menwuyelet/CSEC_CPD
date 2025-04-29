nums = [6,5,4,8]
sort_nums = sorted(nums)
freq = {}
for i in sort_nums:
   if i in freq:
        continue
    
   freq[i] = sort_nums.index(i)

ans = []

for i in nums:
   ans.append(freq[i])

print(ans)