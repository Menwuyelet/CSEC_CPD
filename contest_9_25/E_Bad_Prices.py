t = int(input())
for _ in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    sorted_days = sorted(days, reverse=True)
    seen = set()
    count = 0
    for i in range(n):
        if days:
            if sorted_days[i] > days[-1] and sorted_days[i] not in seen:
                count += 1
                seen.add(sorted_days[i])
            else:
                while days and sorted_days[i] <= days[-1]:
                    days.pop()
    print(count)
