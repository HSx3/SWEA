import sys
sys.stdin = open("linked_list_숫자_추가.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    series = list(map(int, input().split()))

    for i in range(M):
        idx, number = map(int, input().split())
        series = series[0:idx] + [number] + series[idx:]
        # insert 활용
        # series.insert(idx, number)

    print('#{} {}'.format(test_case, series[L]))
