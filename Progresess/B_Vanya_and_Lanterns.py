n, l = map(int,input().split())
ln = list(map(int, input().split()))
ln.sort()
front = 1
rare = 0
ma = 0

while front <= n-1:
    tem = ln[front] - ln[rare]
    ma = max(ma,tem)
    front +=1
    rare += 1
if 0 in ln and l in ln:
    print(f"{ma/2:.10f}")
elif 0 not in ln and l in ln:
    print(f"{max(ln[0], ma/2):.10f}")
elif l not in ln and 0 in ln:
    print(f"{max(l - ln[-1], ma/2):.10f}")
else:
    m = max(ln[0], l - ln[-1])
    print(f"{max(m, ma/2):.10f}")
