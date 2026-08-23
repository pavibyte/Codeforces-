def solution():
    string = input()
    set_len = len(set(string))
    if set_len%2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
solution()