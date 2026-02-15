n = int(input())
stones = list(input().split())
q = int(input())
summ = []
summ.append(int(stones[0]))
for i in range(1, n):
    summ.append(summ[i-1] + int(stones[i]))
summ = [0] + summ
stones.sort()
# print(stones)
revesumm = []
revesumm.append(int(stones[0]))
for i in range(1, n):
    revesumm.append(revesumm[i-1] + int(stones[i]))
revesumm = [0] + revesumm
# print(summ)
# print(revesumm)
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        print(summ[c]-summ[b-1])
    else:
        print(revesumm[c]-revesumm[b-1])
