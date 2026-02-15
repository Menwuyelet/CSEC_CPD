t = int(input())
path = []
for _ in range(t):
    command = input()
    if command == 'pwd':
        ans = ""
        if not path:
            ans = '/'
        for _ in path:
            ans+=(_ + '/')
        print(ans)
    else:
        com = list(command[3:].split('/'))
        # print(com)
        if com[0] == '':
            path = []
        for c in com:
            if c == '..' and path:
                path.pop()
            elif c == ".." and not path:
                path = []
            else:
                path.append(c)
    