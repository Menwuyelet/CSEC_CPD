n = int(input())
for i in range(n):
    command = input()
    if len(command) > 10:
        print(command[0] + str(len(command)-2) + command[-1])
    else:
        print(command)
