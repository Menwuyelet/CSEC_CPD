n, k = map(int,input().split())
odd_num = (n+1)//2

if k <= odd_num:
    print(2*k-1)
else:
    print(2*(k-odd_num))
        
    

