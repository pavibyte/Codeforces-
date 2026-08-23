def solution():
    friends_count,fence_height = list(map(int,input().split()))
    friends=list(map(int,input().split()))
    width = 0
    for i in friends:
        if i<= fence_height:
            width+=1
        else:
            width+=2

    print(width)


solution()