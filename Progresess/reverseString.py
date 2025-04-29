l = list(input())
right = len(l)-1
left = 0

while right > left:
    l[right], l[left] = l[left], l[right]
    left +=1
    right -=1
print(l)