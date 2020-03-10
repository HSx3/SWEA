import sys
sys.stdin = open("array2_ladder2.txt")


def game(x, y, distance):
    global min_distance

    visited[x][y] = 9
    queue = []
    queue.append((x, y, distance))

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while len(queue) != 0:
        ax, ay, distance = queue.pop(0)

        if distance > min_distance:
            return ay, distance
        if ax == 0:
            return ay, distance

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
                queue.append((nx, ny, distance + 1))
                break


T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_distance_x = 0
    min_distance = 987654321

    # 도착점 찾기
    for i in range(100):
        visited = [[0]*100 for _ in range(100)]

        if ladder[99][i] == 1:
            answer = game(99, i, 1)

            if min_distance >= answer[1]:
                min_distance_x = answer[0]
                min_distance = answer[1]

    print('#{} {}'.format(test_case, min_distance_x))