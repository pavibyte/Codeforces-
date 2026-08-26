def solution():
    n = int(input())
    median = []
    for i in range(n):
        nums = sorted(list(map(int,input().split())))
        median.append(nums[1])
    for i in range(n):
        print(median[i])

solution()