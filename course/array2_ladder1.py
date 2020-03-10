import sys
sys.stdin = open("array2_ladder1.txt")


def find(x, y):
    visited[x][y] = 9
    queue = []
    queue.append((x, y))

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while len(queue) != 0:
        ax, ay = queue.pop(0)

        if ax == 0:
            return ay
        for i in range(3):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                continue
            if ladder[nx][ny] == 0:
                continue
            if visited[nx][ny] != 0:
                continue
            if ladder[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 9
                queue.append((nx, ny))
                break


T = 10

for test_case in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]

    # 도착점 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            answer = find(99, i)
            break

    print('#{} {}'.format(test_case, answer))
