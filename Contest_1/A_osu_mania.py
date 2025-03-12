num =  int(input())

for i in range(num):
    ans = []
    n = int(input())
    for j in range(n):
        note = list(input())
        tem = note.index("#") + 1
        ans.insert(0, tem)
        
    print(*ans)