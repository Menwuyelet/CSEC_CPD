n = int(input())
if n%2 == 0:
    ans = "love"
else:
    ans = "hate"

feeling = ""
for i in range(1, n+1):
    if i == n and ans == "love":
        feeling+="I love it"
    elif i == n and ans == "hate":
        feeling+= "I hate it"
    elif i%2 == 0:
        feeling+="I love that "
    elif i%2 != 0:
        feeling+="I hate that "

print(feeling)
