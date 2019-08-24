import sys
sys.stdin = open("5515_input.txt")

T = int(input())

calendar = {0:0, 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
check = [3, 4, 5, 6, 0, 1, 2]
for test_case in range(1, T+1):
    m, d = map(int, input().split())

    check_m = m-1
    check_d = d-1
    days = check_d

    for i in range(check_m+1):
        days += calendar[i]

    answer = check.index(days%7)
    print('#{} {}'.format(test_case, answer))