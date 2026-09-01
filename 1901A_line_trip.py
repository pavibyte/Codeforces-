def solution():
    cases = int(input())
    answers = []

    for _ in range(cases):
        n, x = map(int, input().split())
        stations = list(map(int, input().split()))

        maximum = stations[0]

        for i in range(n - 1):
            gap = stations[i + 1] - stations[i]
            maximum = max(maximum, gap)

        last_diff = (x - stations[-1]) * 2
        maximum = max(maximum, last_diff)

        answers.append(maximum)

    for answer in answers:
        print(answer)


solution()