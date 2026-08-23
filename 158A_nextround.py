def solution():
    n,m = map(int,input().split())
    text = input()
    arr = text.split()
    original = list(map(int,arr))
    count = 0
    for i in range(0,n):
        if original[i] > 0:
            if original[i] >= original[m-1]:
                count += 1
    return count

print(solution())