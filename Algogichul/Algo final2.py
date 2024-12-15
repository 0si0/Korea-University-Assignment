N = int(input())


if N % 2 == 0:
    if N == 4:
        print(2)
    else:
        print(int(N / 2 + 2))
else:
    if N == 3:
        print(3)
    else:
        print(2 * N)