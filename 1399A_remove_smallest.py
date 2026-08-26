def solution():
    n = int(input())
    array = []
    for i in range(n):
        count = int(input())
        values = sorted(list(map(int,input().split())))
        # print(values)
        for i in range(count-1):
            if (values[(i+1)] - values[i]) != 1 and (values[(i+1)] - values[i]) != 0:
                array.append("NO")
                break
        else:
            array.append("YES")
    for i in array:
        print(i)

solution()