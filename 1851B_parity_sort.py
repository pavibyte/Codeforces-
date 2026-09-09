def solution():
    n = int(input())
    res = []
    for i in range(n):
        length = int(input())
        array = list(map(int,input().split()))
        sol_raw = []
        for i in array:
            if i%2 == 0:
                sol_raw.append("even")
            else:
                sol_raw.append("odd")
        array = sorted(array)
        sol_sorted = []
        for i in array:
            if i%2 == 0:
                sol_sorted.append("even")
            else:
                sol_sorted.append("odd")
        if sol_raw == sol_sorted:
            res.append("YES")
        else:
            res.append("NO")
    for i in res:
        print(i)

solution()