import sys
sys.stdin = open("list2_색칠하기.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                data[j][k] += color

    count = 0

    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                count += 1
    print('#{} {}'.format(test_case, count))