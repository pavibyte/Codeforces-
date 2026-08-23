def solution():
    k,n,w = list(map(int,input().split()))
    total = 0
    cost_per = 1
    for i in range(1,w+1):
        cost_per = (i*k)
        total += cost_per
    if total>n:
        print(total - n)
    else:
        print(0)
solution()