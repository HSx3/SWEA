import sys
sys.stdin = open('1227_input.txt')


def DFS(x, y):
    global flag
    visited[x][y] = 9

    stack = []
    stack.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(stack) != 0:
        ax, ay = stack.pop()


        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            # 벽
            if nx < 1 or nx >= 99 or ny < 1 or ny >= 99:
                continue
            # 길
            if data[nx][ny] == 1:
                continue
            # 탈출
            if data[nx][ny] == 3:
                flag = 1
                return
            if data[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 9
                stack.append((nx, ny))


T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    # print(data)
    # print(visited)

    flag = 0
    for i in range(1, 99):
        for j in range(1, 99):
            if data[i][j] == 2:
                DFS(i, j)
                break
    print('#{} {}'.format(test_case, flag))