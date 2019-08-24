def combination(no):
    global L, answer, max_score
    check_cal = 0
    check_score = 0

    if no >= len(TK_list):
        for i in range(len(TK_list)):
            check_cal += empty_list[i][1]
            check_score += empty_list[i][0]
            if check_cal > L:
                continue
            if check_cal <= L:
                if max_score < check_score:
                    max_score = check_score
        return
    empty_list[no] = TK_list[no]
    combination(no + 1)
    empty_list[no] = (0, 0)
    combination(no + 1)


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    TK_list = []
    for i in range(N):
        Ti, Ki = map(int, input().split())
        TK_list.append((Ti, Ki))
    # print(TK_list)

    empty_list = [0] * len(TK_list)
    max_score = 0

    combination(0)
    print('#{} {}'.format(test_case, max_score))