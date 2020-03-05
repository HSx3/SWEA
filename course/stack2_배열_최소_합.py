import sys
sys.stdin = open("stack2_배열_최소_합.txt")


def calc(idx):
    global total, min_total

    if total > min_total:
        return

    if idx == N:
        if min_total > total:
            min_total = total
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            total += data[idx][i]
            calc(idx+1)
            visited[i] = False
            total -= data[idx][i]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    total = 0
    min_total = 987654321
    calc(0)

    print('#{} {}'.format(test_case, min_total))







# def calc(n, k, cursum):
#     global min_value
#     if min_value > cursum:
#         min_value = cursum
#
#
# def perm(n, k, cursum):
#     global min_value, N
#     if min_value < cursum:
#         return
#     if k == n:
#         calc(n, k, cursum)
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1, cursum + data[k][arr[k]])
#             arr[k], arr[i] = arr[i], arr[k]
#
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     arr = [0] * N
#     for i in range(N):
#         arr[i] = i
#
#     min_value = 987654321
#
#     perm(N, 0, 0)
#     print('#{} {}'.format(test_case, min_value))