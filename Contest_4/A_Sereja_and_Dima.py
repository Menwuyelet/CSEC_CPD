n = int(input())
cards = list(map(int, input().split()))
left = 0
right = n-1
tot = sum(cards)
serja = 0
turn = 1
while left <= right:
    if turn:
        if cards[left] > cards[right]:
            serja += cards[left]
            left += 1
        else:
            serja += cards[right]
            right -= 1
        turn = 0
    else:
        if cards[left] > cards[right]:
            left += 1
        else:
            right -= 1
        turn = 1
print(serja, tot-serja)