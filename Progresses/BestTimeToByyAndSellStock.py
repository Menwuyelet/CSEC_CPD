prices = [7,6,4,3,1]
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    else:
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit

print(max_profit)