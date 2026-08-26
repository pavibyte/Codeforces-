def solution():
    n = int(input())
    numbers = list(map(int,input().split()))
    sereja,dima = 0,0
    i,j =0,len(numbers)-1
    turn = 0
    while i <= j:
        if turn%2 == 0:
            if numbers[i] > numbers[j]:
                sereja += numbers[i]
                i += 1
            else:
                sereja += numbers[j]
                j -= 1
        else:
            if numbers[i]>numbers[j]:
                dima += numbers[i]
                i += 1
            else:
                dima += numbers[j]
                j -= 1
        turn += 1
    print(sereja, dima)
solution()