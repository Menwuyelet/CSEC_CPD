pages, firstread, limit, additional, prev = map(int, input().split())

if pages == firstread or pages < firstread:
    print(1)
    exit()

count = 1
multipl = 1
pages -= firstread
while pages > 0:
    if amount != limit:
        amount = firstread + (multipl*additional)
    if amount <= limit:
        pages -= (amount - prev)
        count += 1
        multipl += 1
    else:
        amount = limit


print(count)