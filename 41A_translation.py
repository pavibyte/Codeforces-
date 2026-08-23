def solution():
    str1 = input().lower()
    str2 = input().lower()
    if str1[::-1] == str2:
        print("YES")
    else:
        print("NO")


solution()