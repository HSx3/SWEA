import sys
sys.stdin = open("day2_최소합.txt")

def DFS(x, y):
    global answer, temp
    if answer < temp:
        return
    elif x == N-1 and y == N-1:
        answer = temp
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < N and ny < N) and ((nx, ny) not in visited):
                visited.append((nx, ny))
                temp += data[nx][ny]
                DFS(nx, ny)
                temp -= data[nx][ny]
                visited.remove((nx, ny))


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    answer = 987654321
    temp = data[0][0]

    dx = [0, 1]
    dy = [1, 0]
    DFS(0, 0)
    print('#{} {}'.format(test_case, answer))