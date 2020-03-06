import sys
sys.stdin = open("queue_피자_굽기.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    oven = [0]*N
    Ci_idx = []

    for i in range(M):
        Ci_idx.append((Ci[i], i+1))

    for i in range(N):
        oven[i] = Ci_idx.pop(0)


    i = 0
    while len(Ci_idx) != 0:
        oven[i] = (oven[i][0] // 2, oven[i][1])
        if oven[i][0] == 0:
            if len(Ci_idx) != 0:
                pizza = Ci_idx.pop(0)
                oven[0] = pizza
            else:
                break
        oven = oven[1:] + [oven[0]]


    k = 0
    count = 0
    check = []

    for i in range(len(oven)):
        check.append(oven[i][1])

    while len(oven) != 1:
        oven[k] = (oven[k][0] // 2, oven[k][1])
        if oven[k][0] != 0:
            oven = oven[1:] + [oven[0]]
        else:
            oven.pop(0)
            count += 1

    print('#{} {}'.format(test_case, oven[0][1]))

    # k = 0
    # count = 0
    # while count != N:
    #     if oven[k][0] != 0:
    #         oven[k] = (oven[k][0] // 2, oven[k][1])
    #     else:
    #         count += 1
    #     oven = oven[1:] + [oven[0]]

    # break




    # pizza = 0
    # for i in range(len(oven)):
    #     if oven[i][1] >= pizza:
    #         pizza = oven[i][0]
    #
    # print('#{} {}'.format(test_case, pizza+1))


    # while len(Ci_idx) != 0:
    #     i = 0
    #     while i != N:
    #         if oven[i][1] != 0:
    #             oven[i] = (oven[i][0], oven[i][1]//2)
    #         elif oven[i][1] == 0:
    #             if len(Ci_idx) != 0:
    #                 oven[i] = (Ci_idx.pop(0))
    #             else:
    #                 oven = oven[i+1:] + oven[0:i+1]
    #                 print(oven)
    #                 break
    #         i += 1