def solution():
    str1 = input().lower()
    str2 = input().lower()
    if str1<str2:
        return -1
    elif str1>str2:
        return 1
    else:
        return 0

print(solution())