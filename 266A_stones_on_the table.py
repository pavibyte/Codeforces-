def solution():
    no_stones =int(input())
    colors = input().upper()
    count=0
    for i in range(no_stones-1):
        if colors[i] == colors[i+1]:
            count+=1
    print(count)

solution()