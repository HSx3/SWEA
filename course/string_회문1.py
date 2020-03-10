import sys
sys.stdin = open("string_회문1.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8-N+1):
            if data[i][j:j+N] == data[i][j:j+N][::-1]:
                count += 1

            temp = ''
            for k in range(j, j+N):
                temp += data[k][i]
            if temp == temp[::-1]:
                count += 1

    print('#{} {}'.format(test_case, count))
