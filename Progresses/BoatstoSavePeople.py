people = [3,5,3,4]
limit = 5
people.sort()

left, right = 0, len(people)-1
count = 0
while left < right:
    if people[left] + people[right] <= limit:
        count += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(len(people) - count)

# solved within 10 minutes