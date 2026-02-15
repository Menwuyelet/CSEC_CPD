w, h = map(int, input().split())
u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())

if h == 2:
    w += ((h*(h+1))//2 - (u1))
if h ==1:
    w += (h*(h+1))//2
else:
    w += ((h*(h+1))//2 - (u1+u2))
 
if w < 0:
    print(0)
else:
    print(w)


