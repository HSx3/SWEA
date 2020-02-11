import sys
sys.stdin = open('탈주범검거_input.txt')


def check(a, b, c, d, direction):
    # 오른쪽
    if direction == 0:
        if data[c][d] == 1:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 6 or data[a][b] == 7:
                return True
            elif data[a][b] == 2 or data[a][b] == 4 or data[a][b] == 5:
                return False


        elif data[c][d] == 2:
            return False

        elif data[c][d] == 3:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 6 or data[a][b] == 7:
                return True
            elif data[a][b] == 2 or data[a][b] == 4 or data[a][b] == 5:
                return False

        elif data[c][d] == 4:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 6 or data[a][b] == 7:
                return True
            elif data[a][b] == 2 or data[a][b] == 4 or data[a][b] == 5:
                return False

        elif data[c][d] == 5:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 6 or data[a][b] == 7:
                return True
            elif data[a][b] == 2 or data[a][b] == 4 or data[a][b] == 5:
                return False

        elif data[c][d] == 6:
            return False

        elif data[c][d] == 7:
            return False

    # 왼쪽
    if direction == 1:
        if data[c][d] == 1:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 4 or data[a][b] == 5:
                return True
            elif data[a][b] == 2 or data[a][b] == 6 or data[a][b] == 7:
                return False

        elif data[c][d] == 2:
            return False

        elif data[c][d] == 3:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 4 or data[a][b] == 5:
                return True
            elif data[a][b] == 2 or data[a][b] == 6 or data[a][b] == 7:
                return False

        elif data[c][d] == 4:
            return False

        elif data[c][d] == 5:
            return False

        elif data[c][d] == 6:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 4 or data[a][b] == 5:
                return True
            elif data[a][b] == 2 or data[a][b] == 6 or data[a][b] == 7:
                return False

        elif data[c][d] == 7:
            if data[a][b] == 1 or data[a][b] == 3 or data[a][b] == 4 or data[a][b] == 5:
                return True
            elif data[a][b] == 2 or data[a][b] == 6 or data[a][b] == 7:
                return False

    # 아래쪽
    if direction == 2:
        if data[c][d] == 1:
            if data[a][b] == 1 or data[a][b] == 2 or data[a][b] == 5 or data[a][b] == 6:
                return True
            elif data[a][b] == 3 or data[a][b] == 4 or data[a][b] == 7:
                return False
            elif data[a][b] == 4:
                return True
            elif data[a][b] == 5:
                return False
            elif data[a][b] == 6:
                return False
            elif data[a][b] == 7:
                return True

        elif data[c][d] == 2:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return True
            elif data[a][b] == 5:
                return False
            elif data[a][b] == 6:
                return False
            elif data[a][b] == 7:
                return True

        elif data[c][d] == 3:
            return False

        elif data[c][d] == 4:
            return False

        elif data[c][d] == 5:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return True
            elif data[a][b] == 5:
                return False
            elif data[a][b] == 6:
                return False
            elif data[a][b] == 7:
                return True

        elif data[c][d] == 6:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return True
            elif data[a][b] == 5:
                return False
            elif data[a][b] == 6:
                return False
            elif data[a][b] == 7:
                return True

        elif data[c][d] == 7:
            return False

    # 위쪽
    if direction == 3:
        if data[c][d] == 1:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return False
            elif data[a][b] == 5:
                return True
            elif data[a][b] == 6:
                return True
            elif data[a][b] == 7:
                return False

        elif data[c][d] == 2:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return False
            elif data[a][b] == 5:
                return True
            elif data[a][b] == 6:
                return True
            elif data[a][b] == 7:
                return False

        elif data[c][d] == 3:
            return False

        elif data[c][d] == 4:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return False
            elif data[a][b] == 5:
                return True
            elif data[a][b] == 6:
                return True
            elif data[a][b] == 7:
                return False

        elif data[c][d] == 5:
            return False

        elif data[c][d] == 6:
            return False

        elif data[c][d] == 7:
            if data[a][b] == 1:
                return True
            elif data[a][b] == 2:
                return True
            elif data[a][b] == 3:
                return False
            elif data[a][b] == 4:
                return False
            elif data[a][b] == 5:
                return True
            elif data[a][b] == 6:
                return True
            elif data[a][b] == 7:
                return False




def BFS(x, y, time):
    global L
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = []
    q.append((x, y, time))

    while len(q) != 0:
        if time == L:
            return
        ax, ay, time = q.pop(0)
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if data[nx][ny] == 0:
                continue
            if data[nx][ny] != 0 and visited[nx][ny] == 0:
                if check(nx, ny, ax, ay, i):
                    visited[nx][ny] = time+1
                    q.append((nx, ny, time+1))


T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    BFS(R, C, 1)

    count = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                count += 1
    print('#{} {}'.format(test_case, count))