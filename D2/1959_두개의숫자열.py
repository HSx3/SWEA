import sys
sys.stdin = open("1959_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    check = []
    if N < M:
        for i in range(M-N+1):
            check_sum = 0
            for j in range(i, N+i):
                check_sum += Ai[j-i] * Bj[j]
            check.append(check_sum)
    elif N > M:
        for i in range(N-M+1):
            check_sum = 0
            for j in range(i, M+i):
                check_sum += Bj[j-i] * Ai[j]
            check.append(check_sum)
    print(f'#{test_case} {max(check)}')