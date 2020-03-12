import sys
sys.stdin = open("stack1_거듭_제곱.txt")

T = 10

for test_case in range(1, T+1):
    tc = int(input())
    N, M = map(int, input().split())
    answer = 1

    for i in range(M):
        answer *= N

    print('#{} {}'.format(test_case, answer))
