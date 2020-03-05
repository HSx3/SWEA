import sys
sys.stdin = open("stack2_미로.txt")


def search(sx, sy):
    global flag

    maze[sx][sy] = '9'

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if maze[nx][ny] == '3':
            flag = 1
            return
        if maze[nx][ny] == '9':
            continue
        if maze[nx][ny] == '1':
            continue
        search(nx, ny)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [['0']*N for _ in range(N)]

    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                visited[i][j] = '9'
                search(i, j)
                break

    print('#{} {}'.format(test_case, flag))



# def search(sx, sy):
#     global flag
#
#     stack = []
#     stack.append((sx, sy))
#
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#
#     while len(stack) != 0:
#         ax, ay = stack.pop()
#
#         for i in range(3):
#             nx = ax + dx[i]
#             ny = ay + dy[i]
#
#             # 범위 밖
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#
#             # 도착
#             elif maze[nx][ny] == '3':
#                 flag = 1
#                 return
#
#             # 길 x
#             elif maze[nx][ny] == '1':
#                 continue
#
#             # 지난 길
#             elif visited[nx][ny] == '9':
#                 continue
#
#             # 진행
#             elif maze[nx][ny] == '0' and visited[nx][ny] == '0':
#                 visited[nx][ny] = '9'
#                 stack.append((nx, ny))