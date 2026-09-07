def solution():
    n = int(input())
    sol = []
    for i in range(n):
        length,operations = list(map(int,input().split()))
        string = input().upper()
        i= 0
        j = i
        count = 0
        while j<=(length-1):
            if string[i] == 'B':
                count += 1
                i = i + operations
            else:
                i = i+1
            j = i
        sol.append(count)
    for i in sol:
        print(i)
solution()