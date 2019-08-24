import sys
sys.stdin = open("4299_input.txt")

T = int(input())

for test_case in range(1, T+1):
    D, H, M = map(int, input().split())

    oD, oH, oM = 11, 11, 11

    cal_D = D - oD
    cal_H = H - oH
    cal_M = M - oM

    if cal_M < 0:
        cal_H = cal_H-1
        cal_M = 60+cal_M

    if cal_H < 0:
        cal_D = cal_D-1
        cal_H = 24+cal_H

    answer = cal_D * 1440 + cal_H * 60 + cal_M

    if answer < 0:
        answer = -1
    else:
        answer = answer

    print('#{} {}'.format(test_case, answer))
