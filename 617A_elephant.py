def solution():
    destination = int(input())
    if destination <= 5:
        print(1)
    else:
        if destination%5 == 0:
            print(destination//5)
        else:
            print((destination // 5)+1)

solution()