import sys
sys.stdin = open("1217_input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    a, b = map(int, input().split())

    print(f'#{test_case} {a**b}')



# def square(n, t):
#     if t < 1:
#         return 1
#     return n * square(n, t-1)
#
# T = 10
#
# for test_case in range(1, T+1):
#     M = int(input())
#     N, times = map(int, input().split())
#     print('#{} {}'.format(test_case, square(N, times)))