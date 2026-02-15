string = input()
adder = set(["(", "{", "<", "["])
key = {")": "(", "}": "{", "]": "[", ">": "<"}
ans = 0
stack = []
# "{()}[]"
# {(
# print(adder)
for _ in string:
    if _ in adder:
        stack.append(_)
    else:
        if (stack and stack[-1] != key[_]):
            ans += 1
            stack.pop()
        elif stack and stack[-1] == key[_]:
            stack.pop()
        elif not stack:
            print("Impossible")
            exit()

if stack:
    print("Impossible")
else:
    print(ans)