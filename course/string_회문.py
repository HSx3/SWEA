import sys
sys.stdin = open("string_회문.txt")


def check(data):
    global flag

    for i in range(N):
        for j in range(N-M+1):
            if data[i][j:j+M] == data[i][j:j+M][::-1]:
                flag = 1
                answer = ''.join(data[i][j:j+M])
                return answer


def check_transposed(data):
    global flag

    for i in range(N):
        for j in range(N):
            if i < j:
                data[i][j], data[j][i] = data[j][i], data[i][j]

    for i in range(N):
        for j in range(N-M+1):
            if data[i][j:j+M] == data[i][j:j+M][::-1]:
                flag = 1
                answer = ''.join(data[i][j:j+M])
                return answer



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    flag = 0

    while True:
        answer = check(data)
        if flag == 1:
            break

        answer  = check_transposed(data)
        if flag == 1:
            break

    print('#{} {}'.format(test_case, answer))