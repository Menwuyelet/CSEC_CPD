inp = list(map(int, input().split()))
Lim = inp[0]
Bob = inp[1]
count = 0
while Lim<Bob or Lim==Bob:
    Lim = Lim*3
    Bob = Bob*2
    count +=1

print (count)
