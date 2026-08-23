def answer():
    w = int(input())
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"

print(answer())
