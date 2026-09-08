def solution():
    n = int(input())
    sol = []
    for i in range(n):
        length = int(input())
        array = sorted(list(map(int,input().split())))
        i = 0
        j = len(array)-1
        sum = 0
        while i<j:
            # if length%2 != 0:
                sum += max(array[i],array[j])-min(array[i],array[j])
                i += 1
                j -= 1
            # else:
        sol.append(sum)
    for i in sol:
        print(i)

solution()