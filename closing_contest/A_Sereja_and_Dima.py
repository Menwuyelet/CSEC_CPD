n = int(input())
cards = list(map(int, input().split()))
left, right = 0, n-1
serja = 0
dima = 0
turn = 1
while left <= right:
    if turn:
        serja += max(cards[left], cards[right])
        if max(cards[left], cards[right]) == cards[left]:
            left += 1
        else:
            right -= 1
        turn = 0
    else:
        dima += max(cards[left], cards[right])
        if max(cards[left], cards[right]) == cards[left]:
            left += 1
        else:
            right -= 1
        turn = 1
print(serja, dima)