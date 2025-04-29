a = int(input())
b = int(input())
c = int(input())

ab = max(a*b, a+b)
bc = max(c*b, c+b)

first = min(ab, bc)

if first == ab:
    abc = max(ab*c, ab+c)
else:
    abc = max(bc*a, bc+a)

print(abc)