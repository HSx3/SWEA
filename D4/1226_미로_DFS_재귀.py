import sys
sys.stdin = open('1226_input.txt')


def DFS(x, y):
    global flag
    visited[x][y] = 9

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or nx >= 15 or ny < 1 or ny >= 15:
            continue
        if data[nx][ny] == 1:
            continue
        if data[nx][ny] == 3:
            flag = 1
            return
        if data[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 9
            DFS(nx, ny)


T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[0 for _ in range(16)] for _ in range(16)]

    flag = 0
    for i in range(1, 15):
        for j in range(1, 15):
            if data[i][j] == 2:
                DFS(i, j)
                break
    print('#{} {}'.format(test_case, flag))