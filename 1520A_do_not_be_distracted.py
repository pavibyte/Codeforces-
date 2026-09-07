def solution():
    t = int(input())
    sol_arr = []
    for i in range(t):
        n = int(input())
        s = input().upper()
        seen_arr = []
        if n == 1:
            sol_arr.append('YES')
            continue
        for i in range(0,n-1):
            if s[i] == s[i+1]:
                continue
            else:
                if s[i+1] in seen_arr:
                    sol_arr.append('NO')
                    break
                if s[i] not in seen_arr:
                    seen_arr.append(s[i])
                else:
                    sol_arr.append('NO')
                    break
        else:
            sol_arr.append('YES')
    for i in sol_arr:
        print(i)

solution()