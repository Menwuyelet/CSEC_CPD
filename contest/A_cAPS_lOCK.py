s = input()
x = s[0].lower() + s[1:].upper() 
if s.isupper():
    print(s.lower())
elif s[1:].isupper() and s[0].islower() or s.islower() and len(s)==1:
    print(s.capitalize())
else:
    print(s)    