def solution():
    num = int(input())
    count = 0
    while num>1:
        rem = num%10
        if rem == 4 or rem == 7:
            count+=1
            num //= 10
        else:
            num//=10
    if count==4 or count==7:
        print("YES")
    else:
        print("NO")

solution()