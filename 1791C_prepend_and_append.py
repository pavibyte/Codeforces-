def solution():
    t = int(input())
    arr = []
    for i in range(t):
        n = int(input())
        s = input()
        i = 0
        j = n-1
        while i < j:
            if s[i]!=s[j]:
                i += 1
                j -= 1
                n = n-2
            else:
                break
        arr.append(n)
    for i in range(t):
        print(arr[i])

solution()