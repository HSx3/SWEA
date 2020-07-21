import sys
sys.stdin = open("day5_최소_생산_비용.txt")


def DFS(n, check, total):
    global min_value

    if n >= N:
        if min_value >= total:
            min_value = total
        return min_value

    if min_value <= total:
        return

    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                DFS(n+1, check, total+V[n][i])
                check[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    min_value = 987654321
    check = [0]*N
    DFS(0, check, 0)    # n, check, total
    print('#{} {}'.format(test_case, min_value))