import sys
sys.stdin = open("1979_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K)
    # print(data)

    count = 0
    for i in range(N):
        check = 0
        for j in range(N-1):
            # data[i][j] == data[i][j+1] == data[i][j+2] == 1
            if data[i][j] == data[i][j+1] == 1:
                check += 1
        if check+1 == K:
            print(f'check+1 = {check+1}, K = {K}')
            count += 1

    for i in range(N):
        check = 0
        for j in range(N-1):
            if data[j][i] == data[j+1][i] == 1:
                check +=1
        if check+1 == K:
            print(f'check+1 = {check + 1}, K = {K}')
            count += 1

    print(f'#{test_case} {count}')