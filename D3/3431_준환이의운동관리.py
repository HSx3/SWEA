import sys
sys.stdin = open("3431_input.txt")

T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())

    print(f'#{test_case}', end=' ')
    if X < L:
        print(L-X)
    elif X > U:
        print(-1)
    else:
        print(0)



# T = int(input())
# for test_case in range(1, T + 1):
#     L, U, X = map(int, input().split())
#
#     print('#{}'.format(test_case), end=' ')
#     if L <= X <= U:
#         print(0)
#     elif L > X:
#         print(L - X)
#     elif U < X:
#         print(-1)