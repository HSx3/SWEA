import sys
sys.stdin = open("linked_list_수열_합치기.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    series = [list(map(int, input().split())) for _ in range(M)]

    answer = series[0]
    for i in range(1, M):
        for j in range(len(answer)):
            if answer[j] > series[i][0]:
                answer = answer[:j] + series[i] + answer[j:]
                break
        else:
            answer = answer + series[i]
    print('#{}'.format(test_case), end=' ')
    print(*answer[-1:-11:-1])

# 시간초과