piles = [9,8,7,6,5,1,2,3,4]
sort_piles = sorted(piles, reverse=True)
n = len(piles)-int(len(piles)/3)
sum = 0
for i in range(1, n+1, 2):
    
    sum+=sort_piles[i]

print(sum)
