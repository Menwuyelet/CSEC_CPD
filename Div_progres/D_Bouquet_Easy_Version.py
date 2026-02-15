t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    petals = [int(num) for num in input().split()]
    petals.sort()
    s = set()
    first = petals[0]
    last = 0
    ans = 0
    for peta in petals:
        s.add(peta)
        if len(s) <= 2:
            last = peta
            ans += peta

