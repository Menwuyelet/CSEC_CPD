# m = int(input())
# boys = list(map(int, input().split()))
# boys.sort()
# f = int(input())
# girls = list(map(int, input().split()))
# girls.sort()

# i = j = 0
# ans = 0

# while i < m and j < f:
#     if abs(boys[i]- girls[j]) <= 1:
#         ans +=1
#         i +=1
#         j += 1
#     elif boys[i] < girls[j]:
#         i +=1
#     else:
#         j +=1

# print(ans)


m = int(input())
boys = list(map(int, input().split()))
boys.sort()
f = int(input())
girls = list(map(int, input().split()))
girls.sort()
 
i, j = 0, 0
ans = 0
while i < m and j < f:
    if abs(boys[i] - girls[j]) <= 1:
        ans += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1
print(ans)