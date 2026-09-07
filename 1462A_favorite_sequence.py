def solution():
    n = int(input())
    for i in range(n):
        length = int(input())
        array = list(map(int,input().split()))
        sol = []
        i = 0
        j = len(array)-1
        while i<=j:
            if i == j:
                sol.append(array[i])
                break
            sol.append(array[i])
            sol.append(array[j])
            i += 1
            j -= 1
        print(*sol)
solution()
