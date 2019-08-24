import sys
sys.stdin = open("6692_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    answer = 0

    for i in range(N):
        pi, xi = map(float, input().split())
        answer += round(pi * xi, 7)

    print('#{}'.format(test_case), end=' ')
    print("%0.6f" % answer)