def solution():
    sol = []
    n = int(input())
    for i in range(n):
        length = int(input())
        string = input()
        i = 0
        j = i+1
        sol_str = ""
        while i < j:
            if string[i] == string[j]:
                sol_str += string[i]
                if j == len(string) - 1:
                    break
                i = (j+1)
                j = (j+2)
            else:
                j += 1
        sol.append(sol_str)
    for i in sol:
        print(i)

solution()