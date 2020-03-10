import sys
sys.stdin = open("array2_sum.txt")

T = 10

for test_case in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    max_value = 0
    check_1 = 0
    check_2 = 0

    for i in range(100):
        check_3 = 0
        check_4 = 0

        check_1 += data[i][i]
        check_2 += data[i][99-i]

        for j in range(100):
            check_3 += data[i][j]
            check_4 += data[j][i]

        if check_3 >= max_value:
            max_value = check_3
        if check_4 >= max_value:
            max_value = check_4

    if check_1 >= max_value:
        max_value = check_1
    if check_2 >= max_value:
        max_value = check_2


    print('#{} {}'.format(test_case, max_value))