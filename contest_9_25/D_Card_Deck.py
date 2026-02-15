t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))

    max_index = sorted(cards)
    res = []
    seen = set()
    end = n
    
    for i in range(n-1, -1, -1):
        if cards[i] == max_index[-1]:
            res += cards[i:end]
            end = i
            max_index.pop()
        while max_index and max_index[-1] in seen:
            max_index.pop()
        seen.add(cards[i])
        
    
    print(*res)

    