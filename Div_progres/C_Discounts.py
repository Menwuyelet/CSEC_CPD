t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    price = [int(num) for num in input().split()]
    voucher = [int(num) for num in input().split()]

    price.sort(reverse=True)
    voucher.sort(reverse=True)

    ans = sum(price)
    # print(ans)
    last = -1
    for i in range(k):
        if voucher:
            # print(i)
            last = last + voucher.pop()
            if last == len(price):
                ans -= price[-1]
                # print(price[-1])
            elif last < len(price):
                ans -= price[last]
                # print(price[last])
                # print(ans)
    print(ans)