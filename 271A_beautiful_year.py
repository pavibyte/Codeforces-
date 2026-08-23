def solution():
    year = int(input())
    # print(len(set(str(year))))
    while year > 0:
        year += 1
        check = len(set(str(year)))
        if 4 == check:
            print(year)
            break

solution()