#Menwuyelet_ICPC_Temesgen
n = int(input())
ans = ["*"]*n
j = 0
for i in range((n//2)+1):
    ans[(n//2)] = "D"
    if j < (n//2)+1:

        ans[((n//2)) + j] = "D"
        ans[((n//2)) - j] = "D"
    j+=1
    print("".join(ans))
i = (n//2)+1
x = 0
while i < n:
    if x < (n//2)+1:
        ans[x] = "*"
        ans[-(x+1)] = "*"
        i+=1
        x+=1
    print("".join(ans))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    