import sys
sys.stdin = open('활주로건설_input.txt')


def runway(x, y, length, flag):
    dx = [0, 0]
    dy = [-1, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if data[nx][ny] == data[x][y] - 1 and visited[nx][ny] == 0:
            flag = 1
            visited[nx][ny] = 9
            runway(nx, ny, length+1, flag)
        if data[nx][ny] == data[x][y] and visited[nx][ny] == 0:
            visited[nx][ny] = 9
            runway(nx, ny, length+1, flag)



T = int(input())

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    print(data)
    check = []
    temp = 0
    for i in range(N):
        a = data[i].index(max(data[i]))
        visited[i][a] = 9
        runway(a, 0, 0, 0)

