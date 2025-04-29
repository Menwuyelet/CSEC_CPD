t = int(input())
for i in range(t):
    num = int(input())
    nstring = str(num)
    ans = []
    for i in range(len(nstring)):
        if nstring[i] != 0:
            roundnum = int(nstring[i] + "0" * (len(nstring)-i-1))
            ans.append(roundnum)
    
    ans1 = []
    for _ in ans:
        if _ != 0:
            ans1.append(_)
    print(len(ans1))
    print(*ans1)
    