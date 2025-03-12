n = int(input())

new = n+1
"""x = len(set(str(new)))
while x < 4:
    new +1
print(new)"""
while True:
    if len(set(str(new))) == 4:
        print(new)
        break
    else:
        new +=1