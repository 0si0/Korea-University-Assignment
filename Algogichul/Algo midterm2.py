N = int(input())


while 1:
    if N % 2 == 0:
        if N // 2 < 10:
            print(2)
            break
    divide = 3
    tmp = N

    even = N // divide

    num = []
    for i in range(divide):
        num.append(0)

    if divide % 2 != 0:
        for i in range(divide):
            if i != divide-1 :
                num[i] = even
                tmp -= even
            else:
                num[i] = tmp
        if tmp >= 10:
            continue
        else:
            print(divide)
            break
    else:
        for i in range(divide):
            if i < divide // 2:
                num[i] = even
                tmp -= even
            else:
                break
        if tmp % (divide // 2) == 0:
            for i in range(divide//2, divide):
                num[i] = tmp // (divide // 2)
        else:
            continue
        if num[-1] <= 10:
            print(divide)


    divide += 1


    

