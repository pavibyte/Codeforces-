def solution():
    stops_count = int(input())
    capacity = 0
    max_capacity = 0
    curr_capacity = 0

    for i in range(stops_count):
        exit,stops = list(map(int,input().split()))
        capacity = capacity - exit
        capacity = capacity + stops
        curr_capacity = capacity
        max_capacity = max(max_capacity,curr_capacity)

    print(max_capacity)

solution()