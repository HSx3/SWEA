import sys
sys.stdin = open("queue_미로2.txt")


def find(x, y):
    global answer
    queue = []
    queue.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(queue):
        ax, ay = queue.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if maze[nx][ny] == 3:
                answer = 1
                return

            if nx < 1 or nx >= 98 or ny < 1 or ny >= 98:
                continue
            if maze[nx][ny] == 1:
                continue
            if visited[nx][ny] == 9:
                continue
            if maze[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 9
                queue.append((nx, ny))



T = 10

for test_case in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    answer = 0
    visited[1][1] = 9
    find(1, 1)
    print('#{} {}'.format(test_case, answer))
