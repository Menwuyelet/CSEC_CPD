n = int(input())
students = [int(num) for num in input().split()]
from collections import Counter
counter = Counter(students)
seen = set()
max_ = 0
for num in students:
    if num not in seen:
        seen.add(num)
        temp = 0
        # curr = num
        # print(curr)
        for i in range(0,6):
            if num+i in counter:
                temp += counter[num + i]
                # curr += 1
        max_ = max(max_, temp)

                

print(max_)