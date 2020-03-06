import sys
sys.stdin = open("queue_미로의_거리.txt")


def search(sx, sy, distance):

    queue = []
    queue.append((sx, sy, distance))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(queue) != 0:
        x, y, distance = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            elif maze[nx][ny] == 3:
                return distance
            elif maze[nx][ny] == 1:
                continue
            elif visited[nx][ny] == 9:
                continue
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 9
                queue.append((nx, ny, distance+1))
    return 0



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                visited[i][j] = 9
                answer = search(i, j, 0)
                break

    print('#{} {}'.format(test_case, answer))