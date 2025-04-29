theset = list(input())
freq = {}
count = 0
for _ in theset:
    if _ not in freq and _.isalpha(): 
        count += 1
        freq[_] = 1
print(count)