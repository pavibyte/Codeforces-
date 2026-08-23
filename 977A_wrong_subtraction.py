def solution():
    num,time=list(map(int,input().split()))
    for i in range(0,time):
        if num%10 != 0:
            num-=1
        else:
            num//=10
    print(num)
solution()