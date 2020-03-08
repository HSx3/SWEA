import sys
sys.stdin = open("linked_list_암호.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    password = list(map(int, input().split()))
    idx = 0

    for i in range(1, K+1):
        idx += M
        if idx < N:
            password.insert(idx, password[idx-1] + password[idx])
        else:
            if idx % N == 0:
                password.insert(idx, password[-1] + password[0])
            else:
                idx = idx % N
                password.insert(idx, password[idx-1] + password[idx])
        N += 1

    print('#{}'.format(test_case), end=' ')
    print(*password[-1:-11:-1])