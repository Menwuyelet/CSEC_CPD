t = int(input())
for i in range(t):
    n = int(input())
    a = list(input().split(" "))
    b = list(input().split(" "))
    c = list(input().split(" "))
    
    dic = {}
    for word in a:
        dic[word] = 1
    for word in b:
        if word in dic:
            dic[word] +=1
        else:
            dic[word] = 1
    for word in c:
        if word in dic:
            dic[word] +=1
        else:
            dic[word] = 1
    pa = n*3
    pb = n*3
    pc = n*3
    for word in a:
        if dic[word] != 1:
            pa -= dic[word]
    for word in b:
        if dic[word] != 1:
            pb -= dic[word]
    for word in c:
        if dic[word] != 1:
            pc -= dic[word]
        

    """for word in b:
        if word in dic:
            pa -=2
            pb -=2
            dic[word] +=1
        else:
            dic2[word] = 1
    for word in c:
        if word in dic and dic[word] == 2:
            pa -=1
            pb -=1
            pc -=3
        elif word in dic and dic[word] == 1:
            pa -=2
            pc -=2
        elif word in dic2 and dic2[word] == 1:
            pb -=2
            pc -=2"""
    
    print(pa, pb, pc)

