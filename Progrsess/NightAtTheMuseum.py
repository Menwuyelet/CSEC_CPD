s = input() 

current = 'a'  
count = 0

for i in s:
    f = abs(ord(i) - ord(current))
    b= 26 - f
    count += min(f, b)
    current = i

print(count)
