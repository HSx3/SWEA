import sys
sys.stdin = open("2001_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    answer = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    fly += data[x][y]
            answer.append(fly)

    print(f'#{test_case} {max(answer)}')