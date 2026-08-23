def solution():
    num = int(input())
    words = [input() for _ in range(num)]
    for word in words:
        length = len(word)
        if length > 10:
            length = length - 2
            print(word[0]+str(length)+word[-1])
        else:
            print(word)

solution()