import sys
sys.stdin = open('1210_input.txt')


def ladder(x, y):
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while True:
        if x == 0:
            return y
        else:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                    continue
                if data[nx][ny] == 0:
                    continue
                if data[nx][ny] == 1:
                    data[nx][ny] = 9
                    x = nx
                    y = ny
                if data[nx][ny] == 9:
                    continue


T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if data[99][i] == 2:
            print('#{} {}'.format(test_case, ladder(99, i)))
            break