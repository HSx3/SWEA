import sys
sys.stdin = open("list1_구간합.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    max_sum = -987654321
    min_sum = 987654321

    for i in range(N-M+1):
        if sum(data[i:i+M]) >= max_sum:
            max_sum = sum(data[i:i+M])
        if sum(data[i:i+M]) <= min_sum:
            min_sum = sum(data[i:i+M])

    print('#{} {}'.format(test_case, max_sum-min_sum))