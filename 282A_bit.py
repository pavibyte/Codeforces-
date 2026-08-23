def solution():
    n = int(input())
    sol = 0
    for i in range(0,n):
        bit = input()
        if "++" in bit:
            sol += 1
        elif "--" in bit:
            sol -= 1
    print(sol)

solution()