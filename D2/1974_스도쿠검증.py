import sys
sys.stdin = open("1974_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]

    flag = 1
    check_x1 = []
    check_x2 = []
    for i in range(9):
        check_row = []
        check_col = []

        for j in range(9):
            if data[i][j] not in check_row:
                check_row.append(data[i][j])
            if data[j][i] not in check_col:
                check_col.append(data[j][i])
        if len(check_row) != 9:
            flag = 0
            break
        if len(check_col) != 9:
            flag = 0
            break

    for i in range(0, 9, 3):
        check = []
        for j in range(0, 9, 3):
            for x in range(3):
                for y in range(3):
                    if data[x+i][y+j] not in check:
                        check.append(data[x+i][y+j])
            if len(check) != 9:
                flag = 0
                break
    print(f'#{test_case} {flag}')
