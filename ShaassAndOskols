n = int(input())
wi = list(map(int, input().split()))
sh = int(input())

for i in range(sh):
    s = list(map(int, input().split()))
    if s[0] > 1 and s[0] < len(wi):
        wi [s[0]-2] += s[1]-1
        wi [s[0]] += wi[s[0]-1] - s[1]
        wi [s[0]-1] = 0
    elif s[0] == 1 and n > 1:
        wi [s[0]] += wi[s[0]-1] - s[1]
        wi [s[0]-1] = 0
    elif s[0] == len(wi) and n > 1:
        wi [s[0]-2] += s[1]-1
        wi [s[0]-1] = 0
    wi[s[0] - 1] = 0
for i in wi:
    print(i)
