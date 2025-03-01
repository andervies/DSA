def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in bracket_map:
            if not stack or stack.pop() != bracket_map[c]:
                return False

        else:
            stack.append(c)

    return not stack

print(isValid( "()[]{}[()]"))