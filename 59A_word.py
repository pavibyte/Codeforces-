def solution():
    string = input()
    up,low = 0,0
    for i in string:
        if i.isupper():
            up+=1
        else:
            low+=1
    if up>low:
        print(string.upper())
    else:
        print(string.lower())




solution()