def solution():
    games_count = int(input())
    wins = input().upper()
    an,dav = 0,0
    for i in range(len(wins)):
        if wins[i] == "A":
            an+=1
        else:
            dav+=1
    if an>dav:
        print("Anton")
    elif dav>an:
        print("Danik")
    else:
        print("Friendship")


solution()