height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height)-1
maxi = 0
while left < right:
    y = min(height[left], height[right])
    x = right - left
    maxi = max(maxi, y*x)
    if height[left] < height[right]:
        left +=1
    else:
        right -=1
    
print(maxi)

