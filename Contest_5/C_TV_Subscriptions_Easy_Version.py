t = int(input())
for _ in range(t):
    numOfDays, numOfShows, numOfConsiquetiveDays = map(int, input().split())
    shows = list(map(int, input().split()))
    i = 0
    j = 0
    ans = float('inf')
    while i < numOfDays and j <= numOfDays-numOfConsiquetiveDays:
        seen = set()
        while i - j < numOfConsiquetiveDays and i < numOfDays:
            if shows[i] not in seen:
                seen.add(shows[i])
            i+=1
        ans = min(ans, len(seen))
        j+=1
        i = j
    print(ans)