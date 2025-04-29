skill = [1,1,2,3]
skill.sort()
left = 0
right = len(skill)-1
team_skill = skill[left] + skill[right]
ans = 0
while left < right:
    if team_skill != skill[left] + skill[right]:
        ans = -1
        break
    else:
        ans += skill[left]*skill[right]
    left+=1
    right-=1
print(ans)

## solved within 12 mins