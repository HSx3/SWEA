import sys
sys.stdin = open('1211_input.txt')


def ladder(x, y):
    distance = 1
    visited[x][y] = distance

    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while True:
        if x == 0:
            return (visited[1][y]+1, y)
        else:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                    continue
                if data[nx][ny] == 0:
                    continue
                if data[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    # print(visited[nx][ny])
                    # distance += 1
                    x = nx
                    y = ny
                if visited[nx][ny] != 0:
                    continue


T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    goals = []
    check = []
    for i in range(100):
        if data[0][i] == 1:
            check.append(i)
        if data[99][i] == 1:
            visited = [[0 for _ in range(100)] for _ in range(100)]
            a = ladder(99, i)
            goals.append(a)
    goals.sort()
    print('#{} {}'.format(test_case, goals[0][1]))