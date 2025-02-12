stack = []
cto = {")" : "(", "}" : "{", "]" : "["}

s = "{A+B}(C)[{D+E}(F)]"

for c in s:
    if c in cto:
        if stack and stack[-1] == cto[c]:
            stack.pop()
        else:
            print("Invalid parenthesis")
            exit()
    elif c in cto.values():
        stack.append(c)
print("Valid") if not stack else print("Invalid")