import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        idx += 3

        # 1. Range with 0 operations
        ans = max(a, b, c) - min(a, b, c)

        # 2. Try replacing 'a' with b + c
        ra = max(b + c, b, c) - min(b + c, b, c)

        # 3. Try replacing 'b' with a + c
        rb = max(a, a + c, c) - min(a, a + c, c)

        # 4. Try replacing 'c' with a + b
        rc = max(a, b, a + b) - min(a, b, a + b)

        ans = min(ans, ra, rb, rc)
        out.append(str(ans))

    print('\n'.join(out))


if __name__ == '__main__':
    solve()